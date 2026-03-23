from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.orders.models import Order
from apps.payments.services.payment_service import create_payment, process_payment
from apps.payments.serializers.payment_serializer import PaymentSerializer


class PaymentViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        order_id = request.data.get("order")
        print('order_id>>>>>>>>>>>>>>>>>', order_id)
        order = Order.objects.get(id=order_id, user=request.user)
        print('order>>>>>>>>>>>>>>>>>', order)
        payment = create_payment(order)

        # simulate success (later integrate real gateway)
        payment = process_payment(payment, success=True)

        return Response(PaymentSerializer(payment).data)