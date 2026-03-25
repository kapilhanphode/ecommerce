from decimal import Decimal
from apps.payments.models import Payment, Refund
from apps.orders.models import Order
from apps.wallet.models import Wallet, WalletTransaction
from apps.notifications.services.email_service import send_email
from apps.notifications.utils.email_templates import refund_processed_email
from rest_framework.exceptions import ValidationError
from django.db import transaction


from django.db import transaction

@transaction.atomic
def process_refund(order):

    order = Order.objects.select_for_update().get(id=order.id)

    if order.status == "refunded":
        return Decimal("0")

    payments = Payment.objects.filter(order=order, vendor__isnull=False)

    total_refund = Decimal("0")

    for payment in payments:
        vendor = payment.vendor
        refund_amount = payment.vendor_earning

        wallet = Wallet.objects.select_for_update().filter(user=vendor).first()

        if wallet:
            if wallet.balance < refund_amount:
                raise ValidationError({"message": "Insufficient balance"})

            wallet.balance -= refund_amount
            wallet.save()

            WalletTransaction.objects.create(
                wallet=wallet,
                amount=refund_amount,
                type="debit",
                description=f"Refund for order {order.id}"
            )

        total_refund += refund_amount

    Refund.objects.create(
        order=order,
        amount=total_refund,
        status="processed"
    )

    order.status = "refunded"
    order.save()

    email = refund_processed_email(order)
    send_email(email["subject"], email["message"], [order.user.email])

    return total_refund
