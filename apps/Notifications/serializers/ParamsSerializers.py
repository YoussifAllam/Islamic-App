from rest_framework.serializers import Serializer, IntegerField


class NotificationIDValidator(Serializer):
    notification_id = IntegerField()
