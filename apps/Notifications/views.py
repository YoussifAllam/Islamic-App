from rest_framework.views import APIView
from .db_queries import selectors, services
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GetUserNotifications(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Response_data, Response_status = selectors.get_user_notifications(request)
        return Response(Response_data, Response_status)


class MarkSpecificNotificationAsRead(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Response_data, Response_status = services.mark_specific_notification_as_read(
            request
        )
        return Response(Response_data, Response_status)


class MarkAllNotificationsAsRead(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Response_data, Response_status = services.mark_all_notifications_as_read(
            request
        )
        return Response(Response_data, Response_status)


"""
from django.shortcuts import render
from .Tasks import notifications_tasks
def test_notification_view(request, user_id, message, subject):
    notifications_tasks.send_notification(user_id=user_id, message=message, subject=subject)
    return Response({'status': 'Notification sent'})

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    return render(request, 'login.html')


def index(request):
    token = request.session.get('access_token', '')  # Retrieve token from session (or any source)
    # if request.user.is_authenticated:
    #     notifications = NotificationsModel.objects.filter(user=request.user).order_by('-created_at')
    # else:
    #     notifications = []

    # return render(request, 'test_notifications.html', {'notifications': notifications}, {'token': token})
    return render(request, 'test_notifications.html', {'token': token})
"""
