from ..serializers import OutputSerializers
from .. import models
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


def get_user_notifications(request: Request) -> tuple[dict, int]:
    user = request.user
    notifications = models.NotificationsModel.objects.filter(user=user).order_by(
        "-created_at"
    )

    number_of_notifications = request.GET.get("number_of_notifications", None)

    if number_of_notifications:
        notifications = notifications[: int(number_of_notifications)]

    serializer = OutputSerializers.NotificationsSerializer(notifications, many=True)
    return ({"status": "success", "data": serializer.data}, HTTP_200_OK)


def get_notification(request: Request) -> tuple[dict, int]:
    notification_id = request.data["notification_id"]
    try:
        target_notification_obj = models.NotificationsModel.objects.get(
            id=notification_id, user=request.user
        )
    except models.NotificationsModel.DoesNotExist:
        return (
            {"status": "error", "error": "Notification not found"},
            HTTP_400_BAD_REQUEST,
        )
    return ({"target_notification_obj": target_notification_obj}, HTTP_200_OK)


def get_user_all_notifications(request: Request) -> tuple[dict, int]:
    try:
        target_notifications_instances = models.NotificationsModel.objects.filter(
            user=request.user
        )
    except models.NotificationsModel.DoesNotExist:
        return (
            {"status": "error", "error": "Notification not found"},
            HTTP_400_BAD_REQUEST,
        )
    return (
        {"target_notifications_instances": target_notifications_instances},
        HTTP_200_OK,
    )
