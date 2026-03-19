from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet
from .views import ShipmentViewSet

router = DefaultRouter()
router.register("address", AddressViewSet, basename="address")

urlpatterns = [
    path("", include(router.urls)),
    path("shipment/", ShipmentViewSet.as_view({"post": "create"})),
]
