from django.urls import path
from . import views


urlpatterns = [
    path("get_all_notifications/", views.GetUserNotifications.as_view()),
    path("mark_notification_as_read/", views.MarkSpecificNotificationAsRead.as_view()),
    path("mark_all_notifications_as_read/", views.MarkAllNotificationsAsRead.as_view()),
]


"""
    from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
    path('test-notifications_page/', views.index, name='test_notifications'),
    path(
        'test-notification/<str:user_id>/<str:message>/<str:subject>/',
        views.test_notification_view, name='test_notification_page'
    ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.login, name='login'),
"""
