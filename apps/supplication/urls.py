from django.urls import path
from . import views


urlpatterns = [
    path(
        "get-all-supplication/",
        views.supplicationViewSet.as_view({"get": "get_all_supplication"}),
        name="get-all-supplication",
    ),
]
