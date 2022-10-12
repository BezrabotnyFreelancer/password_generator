from rest_framework import serializers
from main.models import TempGenPassword
from storage.models import PasswordStorage


class SaveGenPasswordInStorageSerializer(serializers.Serializer):
    site = serializers.URLField()


class PasswordGenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempGenPassword
        fields = ['id', 'password']


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordStorage
        fields = ['id', 'site', 'password']
