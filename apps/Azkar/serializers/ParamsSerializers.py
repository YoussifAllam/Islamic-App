from rest_framework.serializers import Serializer, UUIDField


class AzkersParamsSerializer(Serializer):
    category_uuid = UUIDField(required=True)
