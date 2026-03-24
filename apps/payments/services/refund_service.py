from decimal import Decimal
from apps.payments.models import Payment, Refund
from apps.wallet.models import Wallet, WalletTransaction
from apps.notifications.services.email_service import send_email
from apps.notifications.utils.email_templates import refund_processed_email

def process_refund(order):
    payments = Payment.objects.filter(order=order, vendor__isnull=False)

    total_refund = Decimal("0")

    for payment in payments:
        vendor = payment.vendor
        refund_amount = payment.vendor_earning

        wallet = Wallet.objects.filter(user=vendor).first()

        if wallet:
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

    # update order
    order.status = "refunded"
    order.save()
    email = refund_processed_email(order)
    send_email(email["subject"], email["message"], [order.user.email])

    return total_refund