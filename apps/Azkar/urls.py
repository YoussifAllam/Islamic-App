from django.urls import path
from . import views


urlpatterns = [
    path(
        "get-azkar-categories/",
        views.AzkarCategoriesViewSet.as_view({"get": "get_azkar_categories"}),
        name="get_azkar_categories",
    ),
    path(
        "get-azkar-by-category/",
        views.AzkarViewSet.as_view({"get": "get_azkar_by_category"}),
        name="get-azkar-by-category",
    ),
]
