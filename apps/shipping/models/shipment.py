from django.db import models
from apps.core.models import BaseModel
from apps.orders.models import Order
from apps.shipping.models.address import Address


class Shipment(BaseModel):
    STATUS_CHOICES = (
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("out_for_delivery", "Out for Delivery"),
        ("delivered", "Delivered"),
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    tracking_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="processing")

    def __str__(self):
        return str(self.id)