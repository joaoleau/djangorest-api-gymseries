from users.models import User
from django.db.models import Q
from users.choices import UserTypeChoice
from django.contrib.auth.hashers import make_password
from rest_framework import status, exceptions


class UserService:
    def create_user(self, data) -> User:
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(Q(username=username) or Q(email=email)).exists():
            raise exceptions.APIException(
                detail="Já existe um usuário com esse username/email"
            )

        password = make_password(password)

        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            full_name=data.get("full_name"),
            type=data.get("type") if data.get("type") else UserTypeChoice.STUDENT,
        )
        return user
