from django.urls import reverse
from django.test import TestCase

from apps.users.models import CustomUser


SUPERUSER_EMAIL = 'admin@webrunners.de'
SUPERUSER_PASSWORD = 'admin'


class TestUserLogin(TestCase):
    fixtures = ['fixtures/users.json']

    def setUp(self):
        self.user = CustomUser.objects.get(email=SUPERUSER_EMAIL)


    def test_login_page(self):
        url = reverse('users:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_unauthorized_cant_access_restricted_content(self):
        url = reverse('users:restricted_content')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


    def test_superuser_login(self):
        url = reverse('users:login')
        response = self.client.post(url,
                                    {'email': SUPERUSER_EMAIL,
                                     'password': SUPERUSER_PASSWORD
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith('/restricted-content/'))
        
