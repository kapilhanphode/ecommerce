from decimal import Decimal

COMMISSION_PERCENTAGE = Decimal("10.0")  # 10%


def calculate_earnings(order):
    total_amount = order.total_amount
    platform_fee = (total_amount * COMMISSION_PERCENTAGE) / 100
    vendor_earning = total_amount - platform_fee

    return platform_fee, vendor_earning