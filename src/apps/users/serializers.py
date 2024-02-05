from rest_framework import serializers


class GetTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

class TokenSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=255)
