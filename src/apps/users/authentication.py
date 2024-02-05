from rest_framework.authtoken.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

class EmailTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        UserModel = get_user_model()
        try:
            user, _ = Token.objects.get(key=key)
        except UserModel.DoesNotExist:
            return None

        if not user.is_active:
            return None

        return user, None

