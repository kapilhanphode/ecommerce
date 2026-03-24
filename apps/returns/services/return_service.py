from apps.returns.models.return_request import ReturnRequest
from apps.payments.services.refund_service import process_refund
from apps.notifications.services.email_service import send_email
from apps.notifications.utils.email_templates import return_requested_email

def create_return(order, reason):
    return_request = ReturnRequest.objects.create(
        order=order,
        reason=reason
    )
    email = return_requested_email(order)
    send_email(email["subject"], email["message"], [order.user.email])
    return return_request

def approve_return(return_request):
    return_request.status = "approved"
    return_request.save()

    # 🔥 Trigger refund after approval
    process_refund(return_request.order)

    return_request.status = "completed"
    return_request.save()

    return return_request
