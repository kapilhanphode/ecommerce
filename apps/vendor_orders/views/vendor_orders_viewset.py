from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.vendor_orders.selectors.vendor_orders_selector import get_vendor_orders
from apps.vendor_orders.serializers.vendor_orders_serializer import VendorOrderSerializer


class VendorOrderViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user

        if user.role != "vendor":
            return Response({"error": "Only vendors allowed"}, status=403)

        orders = get_vendor_orders(user)
        serializer = VendorOrderSerializer(orders, many=True)

        return Response(serializer.data)