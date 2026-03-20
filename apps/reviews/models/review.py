from django.db import models
from apps.core.models import BaseModel
from django.conf import settings
from apps.products.models import Product


class Review(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ("user", "product")