from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .authentication import EmailTokenAuthentication
from .serializers import GetTokenSerializer


# Template Views
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("restricted-content/")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html")


@login_required
def restricted_content(request):
    context = {"email": request.user.email}
    return render(request, "restricted_content.html", context)


# API Views
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = GetTokenSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({settings.API_TOKEN_NAME: token.key}, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([EmailTokenAuthentication])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    user = request.user
    return Response({"email": user.email}, status=status.HTTP_200_OK)
