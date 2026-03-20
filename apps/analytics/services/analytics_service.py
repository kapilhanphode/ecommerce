from apps.orders.models import Order
from django.db.models import Sum, Count


def get_dashboard_stats():
    total_orders = Order.objects.count()
    total_revenue = Order.objects.filter(status="paid").aggregate(
        total=Sum("total_amount")
    )["total"] or 0
    total_users = Order.objects.values("user").distinct().count()
    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_users": total_users,
    }