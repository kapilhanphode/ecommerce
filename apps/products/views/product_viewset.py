from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from django.core.cache import cache

from apps.core.responses import success_response
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
        cache_key = f"product_list_{user.id if user.is_authenticated else 'anon'}"
        queryset = cache.get(cache_key)
        if not queryset:
            queryset = get_active_products().select_related("category").prefetch_related(
                "variants", "images"
            )

            if user.is_authenticated and user.role == "vendor":
                queryset = queryset.filter(created_by=user)
            cache.set(cache_key, queryset, timeout=60)
        return queryset

    def retrieve(self, request, pk=None):
        cache_key = f"product_{pk}"

        product = cache.get(cache_key)

        if not product:
            product = get_product_by_id(pk)
            product = Product.objects.select_related("category").prefetch_related(
                "variants", "images"
            ).get(id=product.id)

            cache.set(cache_key, product, timeout=60)

        serializer = self.get_serializer(product)
        return success_response(data=[serializer.data], message="Product successfully retrieved")
        # return Response(serializer.data)

    def perform_create(self, serializer):
        product = serializer.save(created_by=self.request.user)

        # 🔥 CLEAR CACHE
        cache.delete_pattern("product_list_*")

        return product

    def perform_update(self, serializer):
        product = serializer.save()

        # 🔥 CLEAR CACHE
        cache.delete_pattern("product_list_*")
        cache.delete(f"product_{product.id}")

        return product

    def perform_destroy(self, instance):
        product_id = instance.id

        instance.delete()

        # 🔥 CLEAR CACHE
        cache.delete_pattern("product_list_*")
        cache.delete(f"product_{product_id}")
