"""styleguide_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from prometheus_client import make_wsgi_app

urlpatterns = [
    path("Users/", include("apps.Users.urls")),
    path("Azkar/", include("apps.Azkar.urls")),
    path("supplication/", include("apps.supplication.urls")),
    path("Notifications/", include("apps.Notifications.urls")),
    path("admin/", admin.site.urls),
    path("prometheus/", include("django_prometheus.urls")),
    path("metrics/", csrf_exempt(make_wsgi_app())),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + urlpatterns  # noqa
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # noqa
    )
