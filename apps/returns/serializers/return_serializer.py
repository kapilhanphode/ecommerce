from rest_framework import serializers
from apps.returns.models.return_request import ReturnRequest


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnRequest
        fields = "__all__"
        read_only_fields = ["status"]