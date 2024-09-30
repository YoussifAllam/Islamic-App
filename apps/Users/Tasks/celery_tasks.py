from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_otp_email_task(user_id: int, otp: int, subject: str, message: str) -> None:
    from apps.Users.models import User  # Import User model dynamically within the task

    # Fetch the user object
    user = User.objects.get(id=user_id)

    # Send the email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
