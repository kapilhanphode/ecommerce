from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.wallet.models import Payout

from apps.wallet.services.payout_service import request_payout
from apps.wallet.serializers.payout_serializer import PayoutSerializer


class PayoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payouts = Payout.objects.filter(user=request.user).order_by("-id")
        serializer = PayoutSerializer(payouts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PayoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data["amount"]  # ✅ already Decimal

        payout = request_payout(
            user=request.user,
            amount=amount
        )

        return Response(PayoutSerializer(payout).data)