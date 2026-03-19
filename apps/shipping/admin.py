from django.contrib import admin
from .models import Address, Shipment


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'country')
    list_filter = ('user', 'country')
    search_fields = ('user', 'country')

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'tracking_id', 'status')
    list_filter = ('order', 'status')
    search_fields = ('order', 'status')