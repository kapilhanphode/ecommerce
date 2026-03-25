from apps.inventory.models import Inventory, StockMovement
from rest_framework.exceptions import ValidationError


def create_inventory(variant, stock=0):
    return Inventory.objects.create(variant=variant, stock=stock)


def reserve_stock(inventory, quantity):
    if inventory.available_stock() < quantity:
        raise ValidationError("Not enough stock")

    inventory.reserved_stock += quantity
    inventory.save()

    StockMovement.objects.create(
        inventory=inventory,
        type="reserve",
        quantity=quantity
    )


def release_stock(inventory, quantity):
    inventory.reserved_stock -= quantity
    inventory.save()

    StockMovement.objects.create(
        inventory=inventory,
        type="release",
        quantity=quantity
    )


def deduct_stock(inventory, quantity):
    def deduct_stock(inventory, quantity):
        if inventory.stock < quantity:
            raise Exception("Not enough stock")
        inventory.stock -= quantity
        inventory.save()

    StockMovement.objects.create(
        inventory=inventory,
        type="out",
        quantity=quantity
    )
