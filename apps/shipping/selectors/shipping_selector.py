from apps.shipping.models import Address, Shipment


def get_user_addresses(user):
    return Address.objects.filter(user=user)


def get_shipment_by_order(order):
    return Shipment.objects.filter(order=order).first()