from django.db import models
from apps.wallet.models.wallet import Wallet


class WalletTransaction(models.Model):
    TYPE_CHOICES = (
        ("credit", "Credit"),
        ("debit", "Debit"),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        indexes = [
            models.Index(fields=["wallet"]),
            models.Index(fields=["type"]),
            models.Index(fields=["created_at"]),
        ]