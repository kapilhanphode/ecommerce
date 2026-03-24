from django.db import models
from apps.orders.models import Order
from apps.core.models import BaseModel


class ReturnRequest(BaseModel):
    STATUS_CHOICES = (
        ("requested", "Requested"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("completed", "Completed"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="requested")

    def __str__(self):
        return f"Return {self.order.id} - {self.status}"