from rest_framework import serializers
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


    class Meta:
        model = CustomUser
        # These fields can be included in response or request
        fields = ['email', 'username', 'password', 'token']
