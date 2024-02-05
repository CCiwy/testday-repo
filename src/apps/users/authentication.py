from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

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

