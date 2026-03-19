from rest_framework.viewsets import ModelViewSet
from apps.products.models import Product
from apps.products.serializers.product_serializer import ProductSerializer
from apps.products.selectors.product_selector import get_active_products
from apps.products.filters import ProductFilter
from apps.core.permissions import IsAdminOrReadOnly


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    filterset_class = ProductFilter
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        return get_active_products()