from rest_framework.viewsets import ModelViewSet
from apps.products.models import Category
from apps.products.serializers.category_serializer import CategorySerializer
from apps.core.permissions import IsAdminOrReadOnly


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]