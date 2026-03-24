from apps.orders.models import Order, OrderItem
from apps.cart.models import Cart
from apps.inventory.selectors.inventory_selector import get_inventory_by_variant
from apps.inventory.services.inventory_service import deduct_stock
from apps.notifications.services.email_service import send_email
from apps.notifications.utils.email_templates import order_created_email
from rest_framework.exceptions import ValidationError

def create_order_from_cart(user):
    cart = Cart.objects.filter(user=user).prefetch_related("items__variant").first()
    if not cart or not cart.items.exists():
        raise ValidationError({"cart": "Cart is empty"})
    order = Order.objects.create(user=user)
    total = 0
    for item in cart.items.all():
        price = item.variant.price
        quantity = item.quantity
        inventory = get_inventory_by_variant(item.variant)
        # deduct stock
        deduct_stock(inventory, quantity)
        OrderItem.objects.create(
            order=order,
            variant=item.variant,
            price=price,
            quantity=quantity
        )
        total += price * quantity
    order.total_amount = total
    order.save()
    # clear cart
    cart.items.all().delete()
    email = order_created_email(order)
    send_email(email["subject"], email["message"], [user.email])
    return order
