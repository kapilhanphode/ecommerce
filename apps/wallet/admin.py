from django.contrib import admin
from .models import Wallet, WalletTransaction, Payout


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    list_filter = ('user',)
    search_fields = ('user',)

@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'type', 'amount')
    list_filter = ('type',)
    search_fields = ('wallet',)

@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status')
    list_filter = ('user', 'status')
    search_fields = ('user',)

