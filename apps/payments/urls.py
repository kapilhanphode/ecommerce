from django.urls import path
from rest_framework.routers import DefaultRouter
# from apps.payments.views.payment_viewset import PaymentViewSet
from .views import PaymentViewSet

router = DefaultRouter()
router.register("", PaymentViewSet, basename="payments")

urlpatterns = router.urls