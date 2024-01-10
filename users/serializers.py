from rest_framework import serializers


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)  # serializers.EmailField
    password = serializers.CharField(max_length=250)
    type = serializers.ChoiceField(choices=["Teacher", "Student"], required=False)
    full_name = serializers.CharField(max_length=150)
