from django.db import models
from apps.core.models import BaseModel
from apps.products.models import ProductVariant


class Inventory(BaseModel):
    variant = models.OneToOneField(ProductVariant, on_delete=models.CASCADE, related_name="inventory")
    stock = models.PositiveIntegerField(default=0)
    reserved_stock = models.PositiveIntegerField(default=0)

    def available_stock(self):
        return self.stock - self.reserved_stock

    def __str__(self):
        return str(self.variant)