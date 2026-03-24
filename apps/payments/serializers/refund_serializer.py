from rest_framework import serializers
from apps.payments.models import Refund


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = "__all__"