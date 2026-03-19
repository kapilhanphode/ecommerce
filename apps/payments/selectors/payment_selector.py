from apps.payments.models import Payment


def get_payments_by_order(order):
    return Payment.objects.filter(order=order)