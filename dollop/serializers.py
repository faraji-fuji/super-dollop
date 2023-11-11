from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Entry


class UserSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        return validated_data


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EntrySerializer(serializers.Serializer):
    value = serializers.CharField()

    def create(self, validated_data):
        return validated_data


class GetEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"
