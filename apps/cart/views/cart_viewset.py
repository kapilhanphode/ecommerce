from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.cart.services.cart_service import add_to_cart
from apps.cart.selectors.cart_selector import get_cart_with_items
from apps.products.models import ProductVariant
from apps.cart.models import Cart


class CartViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart = get_cart_with_items(user=request.user)
        if not cart:
            return Response({"items": []})
        from apps.cart.serializers.cart_serializer import CartSerializer
        return Response(CartSerializer(cart).data)

    def create(self, request):
        variant_id = request.data.get("variant")
        quantity = int(request.data.get("quantity", 1))
        variant = ProductVariant.objects.get(id=variant_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item = add_to_cart(cart, variant, quantity)
        return Response({"message": "Added to cart"})