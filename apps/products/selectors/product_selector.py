from apps.products.models import Product


def get_active_products():
    return Product.objects.filter(is_active=True, is_deleted=False).select_related(
        "category"
    ).prefetch_related("variants", "images")