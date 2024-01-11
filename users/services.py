from users.models import User, UserConfirmation
from django.db.models import Q
from users.choices import UserTypeChoice
from django.contrib.auth.hashers import make_password
from rest_framework import exceptions
import string
import random


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
            is_active=False,
            full_name=data.get("full_name"),
            type=data.get("type") if data.get("type") else UserTypeChoice.STUDENT,
        )
        return user

    def get_user(self, **kwargs) -> User:
        try:
            user = User.objects.get(**kwargs)
        except User.DoesNotExist:
            raise exceptions.NotFound(detail="Usuario nao foi encontrado")
        return user


class UserConfirmationService:
    def create(self, email: str) -> UserConfirmation:
        user = UserService().get_user(email=email)
        code = self.get_code(user=user)

        if code:
            if code.is_confirmed:
                raise exceptions.APIException(detail="Usuario ja esta ativo")
            return code

        return UserConfirmation.objects.create(
            user=user,
            code=self.__create_code(),
        )

    def __create_code(self) -> str:
        length = 6
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choice(characters) for _ in range(length))
        return random_string

    def get_code(self, **kwargs) -> UserConfirmation | bool:
        try:
            code = UserConfirmation.objects.get(**kwargs)
            return code
        except UserConfirmation.DoesNotExist:
            return False

    def verify_code(self, code: str) -> bool:
        code = self.get_code(code=code)

        if code and not code.is_confirmed:
            code.is_confirmed = True
            code.save()
            user = code.user
            user.is_active = True
            user.save()
            return True

        return False
