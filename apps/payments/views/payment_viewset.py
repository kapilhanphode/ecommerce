from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound

from apps.core.responses import success_response
from apps.orders.models import Order
from apps.payments.services.payment_service import create_payment, process_payment
from apps.payments.serializers.payment_serializer import PaymentSerializer


class PaymentViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        order_id = request.data.get("order")
        idempotency_key = request.data.get("idempotency_key")

        # ✅ VALIDATION (RAISE, NOT RETURN)
        if not order_id:
            raise ValidationError({"order": "This field is required"})

        if not idempotency_key:
            raise ValidationError({"idempotency_key": "This field is required"})

        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            raise NotFound("Invalid order")

        if order.status != "pending":
            raise ValidationError(
                {"order": f"Only pending orders can be paid. Current status: {order.status}"}
            )

        payment, is_idempotent = create_payment(order, idempotency_key=idempotency_key)

        if not is_idempotent:
            payment = process_payment(payment, success=True)

        data = PaymentSerializer(payment).data
        data["idempotent"] = is_idempotent
        return success_response(data=data, message="Payment successful", status=status.HTTP_201_CREATED)
        # return Response(data, status=status.HTTP_201_CREATED)
