from apps.cart.models import Cart, CartItem
from apps.inventory.selectors.inventory_selector import get_inventory_by_variant
from apps.inventory.services.inventory_service import reserve_stock
from apps.inventory.services.inventory_service import release_stock


def add_to_cart(cart, variant, quantity):
    inventory = get_inventory_by_variant(variant)
    if not inventory:
        raise Exception("Inventory not found")
    # reserve stock first
    reserve_stock(inventory, quantity)
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        variant=variant,
        defaults={"quantity": quantity}
    )
    if not created:
        item.quantity += quantity
        item.save()
    return item


def remove_from_cart(cart, variant):
    item = CartItem.objects.filter(cart=cart, variant=variant).first()
    if not item:
        return
    inventory = get_inventory_by_variant(variant)
    release_stock(inventory, item.quantity)
    item.delete()