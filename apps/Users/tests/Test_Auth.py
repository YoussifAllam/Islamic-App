from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.utils import timezone
from unittest.mock import patch
from ..models import User


class UserTests(APITestCase):  # noqa
    def setUp(self):  # type: ignore
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
            "first_name": "Test",
            "last_name": "User",
            "accept_terms": True,
        }
        self.user = User.objects.create_user(
            username="existinguser",
            email="existinguser@example.com",
            password="password123",
            email_verified=True,
        )

    def test_create_user(self):  # type: ignore
        """Test creating a new user"""
        url = reverse("Signup-list")  # Adjust the URL name if necessary
        response = self.client.post(url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"]["email"], self.user_data["email"])

    def test_create_user_invalid_data(self):  # type: ignore
        """Test creating a user with invalid data"""
        self.user_data["email"] = ""
        url = reverse("Signup-list")  # Adjust the URL name if necessary
        response = self.client.post(url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch(
        "apps.Users.Tasks.Auth_tasks.send_otp_to_user_email"
    )  # Patch the OTP sending function
    def test_confirm_email_valid_otp(self, mock_send_otp):  # type: ignore
        """Test confirming email with a valid OTP"""
        self.user.otp = 1234
        self.user.otp_created_at = timezone.now()
        self.user.save()

        url = reverse("confirm-email")
        response = self.client.post(
            url, {"user_uuid": self.user.uuid, "otp": 1234}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["detail"], "Email confirmed successfully.")

    def test_confirm_email_invalid_otp(self):  # type: ignore
        """Test confirming email with an invalid OTP"""
        self.user.otp = 1234
        self.user.otp_created_at = timezone.now()
        self.user.save()

        url = reverse("confirm-email")
        response = self.client.post(
            url, {"user_uuid": self.user.uuid, "otp": 5678}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_send_reset_otp(self):  # type: ignore
        """Test sending reset OTP"""
        url = reverse("send-reset-otp")
        response = self.client.post(
            url, {"email": "existinguser@example.com"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["detail"], "Reset OTP sent successfully.")

    def test_send_reset_otp_invalid_user(self):  # type: ignore
        """Test sending reset OTP for a non-existing user"""
        url = reverse("send-reset-otp")
        response = self.client.post(
            url, {"email": "nonexisting@example.com"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login_valid(self):  # type: ignore
        """Test login with valid credentials"""
        url = "/Auth/Login/"  # Login path is not named, so use hardcoded path
        response = self.client.post(
            url,
            {"email": "existinguser@example.com", "password": "password123"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("tokens", response.data)

    def test_login_invalid(self):  # type: ignore
        """Test login with invalid credentials"""
        url = "/Auth/Login/"  # Login path is not named, so use hardcoded path
        response = self.client.post(
            url,
            {"email": "nonexisting@example.com", "password": "wrongpassword"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout(self):  # type: ignore
        """Test logging out with token blacklisting"""
        refresh_token = self.user.refresh_tokens.create()  # Mock refresh token creation
        self.client.force_authenticate(user=self.user)
        url = reverse("logout")  # Adjust URL name as needed
        response = self.client.post(
            url, {"refresh_token": refresh_token}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
