from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.orders.models import Order
from apps.shipping.services.shipping_service import create_shipment
from apps.shipping.serializers.shipping_serializer import ShipmentSerializer
from apps.shipping.models import Address


class ShipmentViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        order_id = request.data.get("order")
        address_id = request.data.get("address")
        order = Order.objects.get(id=order_id, user=request.user)
        address = Address.objects.get(id=address_id, user=request.user)
        shipment = create_shipment(order, address)
        return Response(ShipmentSerializer(shipment).data)