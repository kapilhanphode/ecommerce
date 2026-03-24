from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.wallet.selectors.wallet_selector import get_wallet
from apps.wallet.serializers.wallet_serializer import WalletSerializer


class WalletView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        wallet = get_wallet(request.user)

        if not wallet:
            return Response({"balance": 0})

        serializer = WalletSerializer(wallet)
        return Response(serializer.data)