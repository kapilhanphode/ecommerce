from rest_framework import serializers
from apps.orders.models import Order, OrderItem


class VendorOrderItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="variant.product.name")

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price"]


class VendorOrderSerializer(serializers.ModelSerializer):
    items = VendorOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "status", "total_amount", "items"]