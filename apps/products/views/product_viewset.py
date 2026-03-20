from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers.product_serializer import ProductSerializer
from apps.products.selectors.product_selector import (
    get_active_products,
    get_product_by_id
)
from apps.products.filters import ProductFilter


class IsVendorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.role in ["admin", "vendor"]


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsVendorOrAdmin]

    filterset_class = ProductFilter
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        user = self.request.user
        queryset = get_active_products()
        if user.is_authenticated and user.role == "vendor":
            return queryset.filter(created_by=user)
        return queryset

    def retrieve(self, request, pk=None):
        product = get_product_by_id(pk)
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
