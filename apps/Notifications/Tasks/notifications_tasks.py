from .. import models
from apps.Users.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_notification(user_id, message, subject):
    # Save the notification to the database
    user = User.objects.get(id=user_id)
    created_notification = models.NotificationsModel.objects.create(
        user=user, message=message, subject=subject
    )

    # Send the notification via WebSocket
    channel_layer = get_channel_layer()
    group_name = f"user_{user_id}"

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "send_notification",
            "message": message,
            "subject": subject,
            "id": created_notification.id,
        },
    )
