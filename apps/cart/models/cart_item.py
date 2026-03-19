from django.db import models
from apps.core.models import BaseModel
from apps.cart.models.cart import Cart
from apps.products.models import ProductVariant


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cart} | {self.variant}'

    class Meta:
        unique_together = ("cart", "variant")