from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from apps.orders.services.order_service import create_order_from_cart
from apps.orders.selectors.order_selector import get_user_orders
from apps.orders.serializers.order_serializer import OrderSerializer
from apps.orders.models import Order



class OrderViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        orders = get_user_orders(request.user)
        return Response(OrderSerializer(orders, many=True).data)

    def create(self, request):
        order = create_order_from_cart(request.user)
        return Response(OrderSerializer(order).data)

    def retrieve(self, request, pk=None):
        try:
            order = Order.objects.get(id=pk, user=request.user)
        except Order.DoesNotExist:
            raise NotFound("Order not found")

        return Response(OrderSerializer(order).data)