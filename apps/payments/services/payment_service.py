import uuid
from collections import defaultdict
from decimal import Decimal
from apps.payments.models import Payment
from apps.orders.models import Order
from apps.inventory.services.inventory_service import release_stock
from apps.inventory.selectors.inventory_selector import get_inventory_by_variant
from apps.wallet.services.wallet_service import credit_wallet
from apps.payments.services.earnings_service import calculate_earnings
from apps.notifications.services.email_service import send_email
from apps.notifications.utils.email_templates import payment_success_email

COMMISSION_PERCENTAGE = Decimal("10.0")



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

        order = payment.order
        order.status = "paid"
        order.save()
        email = payment_success_email(order)
        send_email(email["subject"], email["message"], [order.user.email])

        # 🔥 NEW LOGIC: SPLIT PER VENDOR
        vendor_totals = defaultdict(Decimal)

        for item in order.items.all():
            vendor = item.variant.product.created_by
            vendor_totals[vendor] += item.price * item.quantity

        # 🔥 CREATE PAYMENT PER VENDOR
        for vendor, total in vendor_totals.items():
            platform_fee = (total * COMMISSION_PERCENTAGE) / 100
            vendor_earning = total - platform_fee

            Payment.objects.create(
                order=order,
                amount=total,
                platform_fee=platform_fee,
                vendor_earning=vendor_earning,
                status="success",
                transaction_id=str(uuid.uuid4()),
                provider=payment.provider,
                vendor=vendor
            )
            credit_wallet(
                user=vendor,
                amount=vendor_earning,
                description=f"Earning from order {order.id}"
            )

    else:
        payment.status = "failed"

        for item in payment.order.items.all():
            inventory = get_inventory_by_variant(item.variant)
            release_stock(inventory, item.quantity)

    payment.save()
    return payment

