from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    total_orders = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_users = serializers.IntegerField()