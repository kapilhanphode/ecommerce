from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from apps.payments.models import Payment


class VendorEarningsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role != "vendor":
            return Response({"error": "Only vendors allowed"}, status=403)

        payments = Payment.objects.filter(
            vendor=user,
            status="success"
        )

        total_earning = sum(p.vendor_earning for p in payments)

        return Response({
            "total_earning": total_earning
        })

# class VendorEarningsView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         user = request.user
#
#         if user.role != "vendor":
#             return Response({"error": "Only vendors allowed"}, status=403)
#
#         payments = Payment.objects.filter(
#             order__items__variant__product__created_by=user,
#             status="success"
#         ).distinct()
#
#         total_earning = sum(p.vendor_earning for p in payments)
#
#         return Response({
#             "total_earning": total_earning
#         })