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


class SignUPViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = InputSerializers.SignUpSerializer
    permission_classes = [IsAdminOrPostOnly]
    lookup_field = "uuid"

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_data = Auth_tasks.send_otp_to_user_email(user)
            return Response(
                {"user": serializer.data, "tokens": token_data}, status=HTTP_201_CREATED
            )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"])
    def confirm_email(self, request):
        Response_data, Response_status = Auth_tasks.conferm_email_using_otp(request)
        return Response(Response_data, status=Response_status)

    @action(detail=False, methods=["post"])
    def send_reset_otp(self, request):
        Response_data, Response_status = Auth_tasks.send_reset_otp(request)
        return Response(Response_data, status=Response_status)


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        Response_data, Response_status = Auth_tasks.Login(request)
        return Response(Response_data, Response_status)


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        Response_data = selectors.get_user_info(request)
        return Response(
            {"status": "success", "data": Response_data}, status=HTTP_200_OK
        )

    def put(self, request):
        Response_data = services.update_user_info(request)
        return Response(Response_data, HTTP_200_OK)


class ForgetPasswordView(APIView):
    def post(self, request):
        Response_data, Response_status = password_tasks.forget_password(request)
        return Response(Response_data, status=Response_status)


class ResetPasswordView(APIView):
    def post(self, request, token):
        Response_data, Response_status = password_tasks.reset_password(request, token)
        return Response(Response_data, status=Response_status)


class PublicApi(APIView):
    authentication_classes = ()
    permission_classes = ()


class GoogleLoginRedirectView(PublicApi):
    def get(self, request, *args, **kwargs):
        google_login_flow = google_auth_tasks.GoogleRawLoginFlowService()

        authorization_url, state = google_login_flow.get_authorization_url()

        request.session["google_oauth2_state"] = state

        # redirect to authorization_url
        return redirect(authorization_url)


class GoogleLoginCallbackView(PublicApi):
    def get(self, request, *args, **kwargs):
        Response_data, Response_status = google_auth_tasks.google_login(request)
        return Response(Response_data, status=Response_status)


class APILogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        Response_data = Auth_tasks.Logout(self, request, *args, **kwargs)
        return Response(Response_data, status=HTTP_200_OK)
