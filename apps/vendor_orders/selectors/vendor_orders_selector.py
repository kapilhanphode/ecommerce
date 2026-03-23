from apps.orders.models import Order


def get_vendor_orders(vendor):
    return Order.objects.filter(
        items__variant__product__created_by=vendor
    ).distinct().prefetch_related("items__variant__product")