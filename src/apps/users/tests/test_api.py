from django.test import TestCase
from django.urls import reverse

from apps.users.models import CustomUser

SUPERUSER_EMAIL = "admin@webrunners.de"
SUPERUSER_PASSWORD = "admin"


class AuthenticationTest(TestCase):
    def setupTestData(self):
        self.user = CustomUser.objects.create_user(
            email=SUPERUSER_EMAIL, password=SUPERUSER_PASSWORD
        )
        self.tokenurl = reverse("api-token")

    def test_get_token_without_data_returns_status_400(self):
        url = reverse("token")
        response = self.client.post(url, {})

        self.assertEqual(response.status_code, 400)

    def test_get_token_with_invalid_data_returns_status_400(self):
        url = reverse("token")
        response = self.client.post(url, {"email": "", "password": ""}, format="json")

        self.assertEqual(response.status_code, 400)

    def test_get_token_with_valid_data_returns_status_200(self):
        url = reverse("token")
        response = self.client.post(
            url, {"email": SUPERUSER_EMAIL, "password": SUPERUSER_PASSWORD}
        )

        self.assertEqual(response.status_code, 200)

    def test_protected_endpoint_without_token_returns_status_401(self):
        url = reverse("api-protected")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_protected_endpoint_with_valid_token_returns_status_200(self):
        url = reverse("token")
        response = self.client.post(
            url, {"email": SUPERUSER_EMAIL, "password": SUPERUSER_PASSWORD}
        )

        token = response.data["access"]
        url = reverse("api-protected")
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {token}")
        self.assertEqual(response.status_code, 200)
