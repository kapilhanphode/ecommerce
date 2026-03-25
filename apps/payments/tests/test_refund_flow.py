from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal

from apps.orders.models.order import Order
from apps.payments.models.payment import Payment
from apps.payments.services.refund_service import process_refund
from apps.wallet.models.wallet import Wallet

User = get_user_model()


class RefundFlowTestCase(TestCase):

    def setUp(self):
        self.customer = User.objects.create_user(
            email="customer@test.com", password="123456", role="customer"
        )
        self.vendor = User.objects.create_user(
            email="vendor@test.com", password="123456", role="vendor"
        )

    def test_refund_flow(self):
        # Create Order
        order = Order.objects.create(
            user=self.customer,
            total_amount=1000,
            status="paid"
        )

        # Create Payment (✅ FIX: add amount)
        Payment.objects.create(
            order=order,
            vendor=self.vendor,
            amount=Decimal("1000.00"),   # ✅ REQUIRED
            vendor_earning=Decimal("900.00"),
            status="success"
        )

        # Create Wallet
        Wallet.objects.create(
            user=self.vendor,
            balance=Decimal("900.00")
        )

        # Refund
        amount = process_refund(order)

        self.assertEqual(amount, Decimal("900.00"))

        wallet = Wallet.objects.get(user=self.vendor)
        self.assertEqual(wallet.balance, Decimal("0.00"))