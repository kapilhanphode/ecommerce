from apps.cart.models import Cart


def get_cart_with_items(user=None, session_id=None):
    if user and user.is_authenticated:
        return Cart.objects.filter(user=user).prefetch_related("items__variant").first()
    return Cart.objects.filter(session_id=session_id).prefetch_related("items__variant").first()