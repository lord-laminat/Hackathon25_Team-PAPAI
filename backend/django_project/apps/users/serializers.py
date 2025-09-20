from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    # TODO: docstring
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


    class Meta:
        model = CustomUser
        # These fields can be included in response or request
        fields = ['email', 'username', 'password', 'token']


class LoginSerializer(serializers.Serializer):
    # TODO: docstring
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }