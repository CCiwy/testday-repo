from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=255)
