from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import get_user_model

class EmailTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
            user = token.user
        except Token.DoesNotExist:
            return None

        if not user.is_active:
            return None

        return user, None

