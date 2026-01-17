from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "bio",
            "is_verified",
            "is_moderator",
        ]


class UserRegisterationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "email", "bio"]
        extra_kwargs = {"password": {"write_only": True}}

    def create_user(self, validated_data):
        return User.objects.create_user(**validated_data)
