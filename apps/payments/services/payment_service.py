import uuid
from apps.payments.models import Payment
from apps.orders.models import Order
from apps.inventory.services.inventory_service import release_stock
from apps.inventory.selectors.inventory_selector import get_inventory_by_variant

def create_payment(order: Order):
    return Payment.objects.create(
        order=order,
        amount=order.total_amount,
        status="pending"
    )


def process_payment(payment: Payment, success=True):
    if success:
        payment.status = "success"
        payment.transaction_id = str(uuid.uuid4())
        # update order
        order = payment.order
        order.status = "paid"
        order.save()
    else:
        payment.status = "failed"
        # release stock back
        for item in payment.order.items.all():
            inventory = get_inventory_by_variant(item.variant)
            release_stock(inventory, item.quantity)
    payment.save()
    return payment
