from apps.wallet.models.wallet import Wallet


def get_wallet(user):
    return Wallet.objects.filter(user=user).first()