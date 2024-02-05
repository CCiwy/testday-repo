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
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from rest_framework.authtoken.models import Token

from .serializers import TokenSerializer, GetTokenSerializer


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


@api_view(["POST"])
def get_token(request):
    serializer = GetTokenSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]
    user = authenticate(email=email, password=password)
    if user is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    token, _ = Token.objects.get_or_create(user=user)
    token_serializer = TokenSerializer({"access": token.key})
    return Response(token_serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    user = request.user
    return Response({"email": user.email}, status=status.HTTP_200_OK)
