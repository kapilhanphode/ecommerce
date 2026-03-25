from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.products.models.product import Product
from apps.products.models.product_variant import ProductVariant
from apps.products.models.category import Category
from apps.inventory.models.inventory import Inventory
from apps.cart.models import Cart, CartItem
from apps.orders.models.order import Order
from apps.wallet.models.wallet import Wallet

User = get_user_model()


class OrderFlowTestCase(TestCase):

    def setUp(self):
        # Users
        self.customer = User.objects.create_user(
            email="customer@test.com", password="123456", role="customer"
        )
        self.vendor = User.objects.create_user(
            email="vendor@test.com", password="123456", role="vendor"
        )

        # ✅ Category (REQUIRED)
        self.category = Category.objects.create(
            name="Test Category"
        )

        # Product
        self.product = Product.objects.create(
            name="Test Product",
            created_by=self.vendor,
            category=self.category   # ✅ FIX
        )

        # Variant
        self.variant = ProductVariant.objects.create(
            product=self.product,
            price=1000,
            sku="SKU1"
        )

        # Inventory
        self.inventory = Inventory.objects.create(
            variant=self.variant,
            stock=10
        )

        # Cart
        self.cart = Cart.objects.create(user=self.customer)
        CartItem.objects.create(
            cart=self.cart,
            variant=self.variant,
            quantity=2
        )

    def test_full_order_flow(self):
        from apps.orders.services.order_service import create_order_from_cart
        from apps.payments.services.payment_service import create_payment, process_payment

        # Create Order
        order = create_order_from_cart(self.customer)
        self.assertEqual(order.total_amount, 2000)

        # Create Payment
        payment, _ = create_payment(order)
        payment = process_payment(payment, success=True)

        # Verify Payment
        self.assertEqual(payment.status, "success")

        # Verify Wallet Credit
        wallet = Wallet.objects.get(user=self.vendor)
        self.assertTrue(wallet.balance > 0)

        # Verify Order Status
        order.refresh_from_db()
        self.assertEqual(order.status, "paid")