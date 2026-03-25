from django.db import models
from apps.core.models import BaseModel
from .product import Product


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")

    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_at_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["product"]),
            models.Index(fields=["sku"]),
            models.Index(fields=["is_active"]),
        ]