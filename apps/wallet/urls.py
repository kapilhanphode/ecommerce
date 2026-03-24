from django.urls import path

from apps.wallet.views.payout_view import PayoutView
from apps.wallet.views.wallet_view import WalletView

urlpatterns = [
    path("", WalletView.as_view()),
    path("payout/", PayoutView.as_view()),
]