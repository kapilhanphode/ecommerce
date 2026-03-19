from apps.cart.models import Cart, CartItem


def add_to_cart(cart, variant, quantity):
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        variant=variant,
        defaults={"quantity": quantity}
    )

    if not created:
        item.quantity += quantity
        item.save()

    return item