from django.db import models
from django.conf import settings
from apps.core.models import BaseModel


class Wallet(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Wallet - {self.user}"

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
        ]