from django.urls import path
from apps.vendor_orders.views.vendor_orders_viewset import VendorOrderViewSet
from apps.vendor_orders.views.vendor_earnings_view import VendorEarningsView

urlpatterns = [
    path("", VendorOrderViewSet.as_view({"get": "list"})),
    path('earnings/', VendorEarningsView.as_view()),
]