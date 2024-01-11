from django.test import TestCase
from rest_framework import exceptions
from users.models import User
from users.services import UserService


class UserServiceTestCasa(TestCase):
    def setUp(self) -> None:
        self.service = UserService()

    def test_create_user(self):
        payload = {
            "username": "teste",
            "email": "teste@email.com",
            "full_name": "Teste",
            "password": "@Teste123",
        }

        user = self.service.create_user(data=payload)

        self.assertIsInstance(user, User)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(email=payload.get("email")).exists())

    def test_create_user_exception_already_user(self):
        User.objects.create(
            username="teste",
            email="teste@email.com",
        )
        payload = {
            "username": "teste",
            "email": "teste@email.com",
            "full_name": "Teste",
            "password": "@Teste123",
        }
        with self.assertRaises(exceptions.APIException) as ctx:
            self.service.create_user(data=payload)

        self.assertEqual(
            ctx.exception.detail.title(), "Já Existe Um Usuário Com Esse Username/Email"
        )
