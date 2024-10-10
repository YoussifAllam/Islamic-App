from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
# router.register(r"SignUp", views.SignUPViewSet, basename="SignUp")

urlpatterns = [
    path("", include(router.urls)),
    # path(
    #     "confirm-email/",
    #     views.SignUPViewSet.as_view({"post": "confirm_email"}),
    #     name="confirm-email",
    # ),

]
