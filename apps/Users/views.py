from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import redirect

from .models import User
from .serializers import InputSerializers
from .permissions import IsAdminOrPostOnly
from .Tasks import Auth_tasks, password_tasks, google_auth_tasks
from .db_queries import selectors, services
from rest_framework.request import Request
from typing import Any
from django.http import HttpResponseRedirect


class SignUPViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = InputSerializers.SignUpSerializer
    permission_classes = [IsAdminOrPostOnly]
    lookup_field = "uuid"

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            _ = Auth_tasks.send_otp_to_user_email(user)
            return Response({"user": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"])
    def confirm_email(self, request: Request) -> Response:
        Response_data, Response_status = Auth_tasks.conferm_email_using_otp(request)
        return Response(Response_data, status=Response_status)

    @action(detail=False, methods=["post"])
    def send_reset_otp(self, request: Request) -> Response:
        Response_data, Response_status = Auth_tasks.send_reset_otp(request)
        return Response(Response_data, status=Response_status)


class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        Response_data, Response_status = Auth_tasks.Login(request)
        return Response(Response_data, Response_status)


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request: Request) -> Response:
        Response_data = selectors.get_user_info(request)
        return Response(
            {"status": "success", "data": Response_data}, status=HTTP_200_OK
        )

    def put(self, request: Request) -> Response:
        Response_data, Response_status = services.update_user_info(request)
        return Response(Response_data, Response_status)


class ForgetPasswordView(APIView):
    def post(self, request: Request) -> Response:
        Response_data, Response_status = password_tasks.forget_password(request)
        return Response(Response_data, status=Response_status)


class ResetPasswordView(APIView):
    def post(self, request: Request, token: str) -> Response:
        Response_data, Response_status = password_tasks.reset_password(request, token)
        return Response(Response_data, status=Response_status)


class UpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        Response_data, Response_status = password_tasks.update_password(request)
        return Response(Response_data, status=Response_status)


class PublicApi(APIView):
    authentication_classes = ()
    permission_classes = ()


class GoogleLoginRedirectView(PublicApi):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        google_login_flow = google_auth_tasks.GoogleRawLoginFlowService()

        authorization_url, state = google_login_flow.get_authorization_url()

        request.session["google_oauth2_state"] = state

        return redirect(authorization_url)


class GoogleLoginCallbackView(PublicApi):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        Response_data, Response_status = google_auth_tasks.google_login(request)
        return Response(Response_data, status=Response_status)


class APILogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        Response_data = Auth_tasks.Logout(self, request, *args, **kwargs)
        return Response(Response_data, status=HTTP_200_OK)
