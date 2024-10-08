from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from django.http import HttpRequest
from rest_framework.request import Request
from ..models import User
from django.contrib.auth.hashers import make_password
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .. import constant
from . import celery_tasks
from user_agents import parse
from ..serializers import ParamsSerializers

current_site = constant.CURRENT_SITE


def get_current_host(request: HttpRequest) -> str:
    protocol = request.is_secure() and "https" or "http"
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)


def forget_password(request: HttpRequest) -> tuple[dict, int]:
    email = request.data.get("email", None)
    if not email:
        return ({"message": "Email missing"}, HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, email=email)
    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes=10)
    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire_date
    user.profile.save()

    subject = "Password reset on {0}".format(current_site)
    reset_link = f"{constant.rest_password_url}?token={token}"
    operating_system, browser_name = get_device_info(request)

    # Use the template creation function to generate the email body
    body = constant.create_password_reset_template(
        f"{user.first_name} {user.last_name}",
        reset_link,
        operating_system,
        browser_name,
    )

    celery_tasks.send_email_task.delay(user.id,  subject, body)
    return (
        {"details": "Password reset sent to {email}".format(email=email)},
        HTTP_200_OK,
    )


def reset_password(request: HttpRequest, token: str) -> tuple[dict, int]:
    data = request.data
    if "password" not in data or "confirmPassword" not in data:
        return (
            {"error": "Password and confirm password missing"},
            HTTP_400_BAD_REQUEST,
        )
    try:
        user = User.objects.get(profile__reset_password_token=token)
    except User.DoesNotExist:
        return ({"error": "Invalid token"}, HTTP_400_BAD_REQUEST)

    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return ({"error": "Token is expired"}, HTTP_400_BAD_REQUEST)

    if data["password"] != data["confirmPassword"]:
        return ({"error": "Password are not same"}, HTTP_400_BAD_REQUEST)

    user.password = make_password(data["password"])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None
    user.profile.save()
    user.save()
    return ({"details": "Password reset done "}, HTTP_200_OK)


def get_device_info(request: HttpRequest) -> tuple[str, str]:
    # Get the User-Agent string from the request headers
    user_agent_string = request.META.get("HTTP_USER_AGENT", "")

    # Parse the User-Agent string
    user_agent = parse(user_agent_string)

    # Get the operating system and browser name
    operating_system = f"{user_agent.os.family} {user_agent.os.version_string}"
    browser_name = f"{user_agent.browser.family} {user_agent.browser.version_string}"

    return operating_system, browser_name


def check_user_password_is_correct(user: User, provided_password: str) -> bool:
    """
    Check if the provided password matches the user's password.
    """
    # target_user = User.objects.get(id=user.id)
    return user.check_password(provided_password)


def update_password(request: Request) -> tuple[dict, int]:
    data = request.data
    ParamsSerializer = ParamsSerializers.UpdateUserPasswordSerializer(
            data=data, context={'request': request}
    )
    if not ParamsSerializer.is_valid():
        return ({"status": "error", "error": ParamsSerializer.errors}, HTTP_400_BAD_REQUEST)

    user = request.user
    validated_data = ParamsSerializer.validated_data
    new_password = validated_data.get('new_password')

    user.set_password(new_password)
    user.save()
    return ({"message": "Password updated successfully."}, HTTP_200_OK)
