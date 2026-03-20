from apps.inventory.models import Inventory


def get_inventory_by_variant(variant):
    return Inventory.objects.filter(variant=variant).first()