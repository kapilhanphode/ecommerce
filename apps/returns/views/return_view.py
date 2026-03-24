from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.accounts.permissions.role_permissions import IsAdmin
from apps.orders.models import Order
from apps.returns.services.return_service import create_return, approve_return
from apps.returns.models.return_request import ReturnRequest


class ReturnRequestView(APIView):
    permission_classes = [IsAuthenticated]

    # Customer creates return
    def post(self, request):
        order_id = request.data.get("order")
        reason = request.data.get("reason")

        order = Order.objects.get(id=order_id)

        return_request = create_return(order, reason)

        return Response({
            "message": "Return requested",
            "id": return_request.id
        })


class ReturnApproveView(APIView):
    permission_classes = [IsAdmin]

    # Admin approves return
    def post(self, request):
        return_id = request.data.get("return_id")

        return_request = ReturnRequest.objects.get(id=return_id)

        approve_return(return_request)

        return Response({
            "message": "Return approved and refund processed"
        })
