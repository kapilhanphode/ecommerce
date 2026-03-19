from django.db import models
from apps.core.models import BaseModel
from .product import Product


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    image = models.ImageField(upload_to="products/")
    is_primary = models.BooleanField(default=False)