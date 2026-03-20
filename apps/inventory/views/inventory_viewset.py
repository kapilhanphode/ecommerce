from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from apps.inventory.models import Inventory
from apps.inventory.serializers.inventory_serializer import InventorySerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAdminUser]