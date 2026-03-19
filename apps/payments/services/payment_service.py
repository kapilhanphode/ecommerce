import uuid
from apps.payments.models import Payment
from apps.orders.models import Order


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

    payment.save()
    return payment
