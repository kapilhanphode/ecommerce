from django.core.cache import cache
from apps.products.models import Product


def get_active_products():
    cache_key = "active_products"
    products = cache.get(cache_key)
    if not products:
        products = Product.objects.filter(is_deleted=False).prefetch_related("variants", "images")
        cache.set(cache_key, products, timeout=60)  # cache for 60 sec
    return products

def get_product_by_id(product_id):
    cache_key = f"product_{product_id}"
    product = cache.get(cache_key)
    if not product:
        product = Product.objects.prefetch_related("variants", "images").get(id=product_id)
        cache.set(cache_key, product, timeout=120)
    return product