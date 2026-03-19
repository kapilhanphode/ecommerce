import uuid
from apps.shipping.models import Shipment


def create_shipment(order, address):
    return Shipment.objects.create(
        order=order,
        address=address,
        tracking_id=str(uuid.uuid4())
    )


def update_shipment_status(shipment, status):
    shipment.status = status
    shipment.save()
    return shipment