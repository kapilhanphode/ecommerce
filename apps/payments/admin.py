from django.contrib import admin
from .models import Payment, Refund


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'vendor', 'amount', 'platform_fee', 'vendor_earning', 'status')
    list_filter = ('status', 'vendor')
    search_fields = ('order', 'vendor')

@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'status')
    list_filter = ('order', 'status')
    search_fields = ('order', 'status')

