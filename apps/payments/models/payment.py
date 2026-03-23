from django.db import models
from apps.core.models import BaseModel
from apps.orders.models import Order


class Payment(BaseModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    )
    PROVIDER_CHOICES = (
        ("razorpay", "Razorpay"),
        ("stripe", "Stripe"),
        ("cod", "Cash on Delivery"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=50, choices=PROVIDER_CHOICES)  # razorpay/stripe later
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vendor_earning = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vendor = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="vendor_payments"
    )

    def __str__(self):
        return str(self.id)