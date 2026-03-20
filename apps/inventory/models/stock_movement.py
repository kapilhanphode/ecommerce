from django.db import models
from apps.core.models import BaseModel
from apps.inventory.models.inventory import Inventory


class StockMovement(BaseModel):
    TYPE_CHOICES = (
        ("in", "Stock In"),
        ("out", "Stock Out"),
        ("reserve", "Reserve"),
        ("release", "Release"),
    )
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="movements")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.type} - {self.quantity}"