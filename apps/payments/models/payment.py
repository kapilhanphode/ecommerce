from django.db import models
from apps.core.models import BaseModel
from apps.orders.models import Order


class Payment(BaseModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=50, default="mock")  # razorpay/stripe later

    def __str__(self):
        return str(self.id)