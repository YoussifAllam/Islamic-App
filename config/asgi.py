import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django")
django_asgi_app = get_asgi_application()

from apps.Notifications.routing import websocket_urlpatterns  # noqa
from config.middleware import JWTAuthMiddleware  # noqa

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": JWTAuthMiddleware(URLRouter(websocket_urlpatterns)),
    }
)
