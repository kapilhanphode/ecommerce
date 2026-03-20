from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.analytics.services.analytics_service import get_dashboard_stats
from apps.analytics.serializers.analytics_serializer import DashboardSerializer


class DashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = get_dashboard_stats()
        serializer = DashboardSerializer(data)
        return Response(serializer.data)