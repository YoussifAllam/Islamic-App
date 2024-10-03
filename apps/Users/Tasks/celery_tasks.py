from celery import shared_task
from django.core.mail import EmailMessage
import logging
# Get an instance of a logger
logger = logging.getLogger('myapp')


@shared_task
def send_email_task(user_id: int, subject: str, message: str) -> None:
    from apps.Users.models import User

    try:
        # Fetch the user object
        user = User.objects.get(id=user_id)

        # Send the email
        email = EmailMessage(
            subject=subject,
            body=message,
            to=[user.email],
        )
        email.content_subtype = "html"  # Set the email content type to HTML
        email.send()
        logger.info(f"Email sent successfully to {user.email}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
