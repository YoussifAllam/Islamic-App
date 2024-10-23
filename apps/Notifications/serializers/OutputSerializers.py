from rest_framework.serializers import (  # noqa
    ModelSerializer,
)
from .. import models


class NotificationsSerializer(ModelSerializer):
    class Meta:
        model = models.NotificationsModel
        fields = ("id", "subject", "message", "is_read", "created_at")
