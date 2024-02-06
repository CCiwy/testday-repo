from rest_framework import serializers
from django.contrib.auth import authenticate


class GetTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg)
            if not user.is_active:
                msg = "User account is disabled."
                raise serializers.ValidationError(msg)
        else:
            msg = "Must include 'email' and 'password'."
            raise serializers.ValidationError(msg)
        attrs["user"] = user
        return attrs


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=255)
