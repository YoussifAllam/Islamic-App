from ..models import User
from rest_framework.request import Request
from ..serializers import OutputSerializers, ParamsSerializers
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from typing import Any


def Create_user(validated_data: dict, unique_username: str) -> User:
    user = User.objects.create_user(
        username=unique_username,
        email=validated_data["email"],
        password=validated_data["password"],
        first_name=validated_data["first_name"],
        last_name=validated_data["last_name"],
        accept_terms=validated_data["accept_terms"],
    )

    return user


def create_user_for_google_login(user_info: dict) -> User:
    user = User.objects.create(
        email=user_info.get("email"),
        username=user_info.get("email"),
        first_name=user_info.get("given_name"),
        last_name=user_info.get("family_name"),
        email_verified=True,
    )
    return user


def check_user_password_is_correct(user: User, provided_password: str) -> bool:
    """
    Check if the provided password matches the user's password.
    """
    # target_user = User.objects.get(id=user.id)
    return user.check_password(provided_password)


def update_user_info(request: Request) -> tuple[dict[str, Any], int]:
    user = request.user
    data = request.data
    serializer = ParamsSerializers.UpdateUserInfoSerializer(data=data)
    if not serializer.is_valid():
        return ({"status": "error", "data": serializer.errors}, HTTP_400_BAD_REQUEST)

    provided_password = request.data.get("password")
    if not check_user_password_is_correct(user=user, provided_password=provided_password):
        return ({"message": "Password is uncorrect"}, HTTP_400_BAD_REQUEST)

    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user.username = data.get("username", user.username)

    # Check if 'profile_picture' is present in the request data
    if "profile_picture" in request.data:
        user.profile_picture = request.data["profile_picture"]

    user.save()
    serializer = OutputSerializers.UserInfoSerializer(user, many=False)
    return (serializer.data, HTTP_200_OK)
