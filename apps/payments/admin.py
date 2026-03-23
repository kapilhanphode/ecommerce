from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'status', 'vendor', 'amount')
    list_filter = ('status', 'vendor')
    search_fields = ('order', 'vendor')
