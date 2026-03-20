from django.contrib import admin
from .models import Inventory, StockMovement


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant', 'stock', 'reserved_stock')
    list_filter = ('variant',)
    search_fields = ('variant',)


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('id', 'inventory', 'type', 'quantity')
    list_filter = ('inventory', 'type',)
    search_fields = ('inventory', 'type',)
