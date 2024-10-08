from rest_framework.serializers import Serializer, CharField


class UpdateUserInfoSerializer(Serializer):
    password = CharField(required=True)
