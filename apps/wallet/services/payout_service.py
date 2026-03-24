from decimal import Decimal
from rest_framework.exceptions import ValidationError
from apps.wallet.models import Wallet, WalletTransaction, Payout


def request_payout(user, amount):
    wallet = Wallet.objects.filter(user=user).first()

    if not wallet or wallet.balance < amount:
        raise ValidationError({"message": "Insufficient balance"})

    print('amount..................',amount)
    # deduct immediately
    wallet.balance -= amount
    wallet.save()

    # create payout
    payout = Payout.objects.create(
        user=user,
        amount=amount,
        status="pending"
    )

    # record transaction
    WalletTransaction.objects.create(
        wallet=wallet,
        amount=amount,
        type="debit",
        description="Payout requested"
    )

    return payout