from django.db import models
from apps.orders.models import Order
from apps.core.models import BaseModel


class Refund(BaseModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("processed", "Processed"),
        ("failed", "Failed"),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Refund {self.order.id} - {self.amount}"

    class Meta:
        indexes = [
            models.Index(fields=["order"]),
            models.Index(fields=["status"]),
        ]