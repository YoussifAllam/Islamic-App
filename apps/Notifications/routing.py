# routing.py
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/notifications/", consumers.NotificationConsumer.as_asgi()),
]
