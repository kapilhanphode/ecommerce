from apps.notifications.tasks import send_email_task


def send_email(subject, message, recipient_list):
    send_email_task.delay(subject, message, recipient_list)