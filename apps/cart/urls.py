from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.cart.views.cart_viewset import CartViewSet

router = DefaultRouter()
router.register("", CartViewSet, basename="cart")

urlpatterns = router.urls