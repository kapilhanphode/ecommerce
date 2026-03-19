from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.orders.views.order_viewset import OrderViewSet

router = DefaultRouter()
router.register("", OrderViewSet, basename="orders")

urlpatterns = router.urls