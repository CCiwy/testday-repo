from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from rest_framework.authtoken.models import Token


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
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(email=email, password=password)
    if user is not None:
        return Response({settings.API_TOKEN_NAME: "token"}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    return Response({"data": "data"}, status=status.HTTP_200_OK)
