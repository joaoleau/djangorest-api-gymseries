from rest_framework import serializers
from .validators import (
    validator_username,
    validator_email,
    validator_password,
)


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, validators=[validator_username])
    email = serializers.CharField(
        max_length=100, validators=[validator_email]
    )  # serializers.EmailField
    password = serializers.CharField(max_length=250, validators=[validator_password])
    type = serializers.ChoiceField(choices=["Teacher", "Student"], required=False)
    full_name = serializers.CharField(max_length=150)
