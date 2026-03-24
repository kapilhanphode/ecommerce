def order_created_email(order):
    return {
        "subject": f"Order #{order.id} Created",
        "message": f"Your order {order.id} has been placed successfully."
    }


def payment_success_email(order):
    return {
        "subject": f"Payment Successful for Order #{order.id}",
        "message": f"Payment received for order {order.id}."
    }


def return_requested_email(order):
    return {
        "subject": f"Return Requested for Order #{order.id}",
        "message": f"Your return request is submitted."
    }


def refund_processed_email(order):
    return {
        "subject": f"Refund Processed for Order #{order.id}",
        "message": f"Refund has been processed."
    }