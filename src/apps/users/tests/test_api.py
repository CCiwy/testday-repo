from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.users.models import CustomUser

SUPERUSER_EMAIL = "admin@webrunners.de"
SUPERUSER_PASSWORD = "admin"


class AuthenticationTest(TestCase):
    fixtures = ["users.json"]
    @classmethod
    def setUpTestData(cls):
        cls.token_url = reverse("users:token")

    def test_get_token_without_data_returns_status_400(self):
        response = self.client.post(self.token_url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_token_with_invalid_data_returns_status_401(self):
        response = self.client.post(
            self.token_url, {"email": "", "password": ""}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_token_with_valid_data_returns_status_200(self):
        response = self.client.post(
            self.token_url,
            {"email": SUPERUSER_EMAIL, "password": SUPERUSER_PASSWORD},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_protected_endpoint_without_token_returns_status_401(self):
        url = reverse("users:protected")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_endpoint_with_valid_token_returns_status_200(self):
        response = self.client.post(
            self.token_url,
            {"email": SUPERUSER_EMAIL, "password": SUPERUSER_PASSWORD},
            format="json",
        )

        token = response.data[settings.API_TOKEN_NAME]
        url = reverse("users:protected")
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], SUPERUSER_EMAIL)
