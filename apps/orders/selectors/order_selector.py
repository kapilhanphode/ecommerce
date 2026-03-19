from apps.orders.models import Order


def get_user_orders(user):
    return Order.objects.filter(user=user).prefetch_related("items__variant")