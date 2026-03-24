from apps.wallet.models.wallet import Wallet
from apps.wallet.models.transaction import WalletTransaction


def credit_wallet(user, amount, description=""):
    wallet, _ = Wallet.objects.get_or_create(user=user)

    wallet.balance += amount
    wallet.save()

    WalletTransaction.objects.create(
        wallet=wallet,
        amount=amount,
        type="credit",
        description=description
    )