from django.test import TestCase
from users.serializers import UserCreateSerializer


class UserCreateSerializerTestCase(TestCase):
    def test_user_serializer_valid(self):
        payload = {
            "username": "teste",
            "email": "teste@email.com",
            "full_name": "Teste",
            "password": "@Teste123",
        }
        serializer = UserCreateSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_user_serializer_invalid(self):
        payload = {
            "full_name": "Teste",
            "password": "@Teste123",
        }
        serializer = UserCreateSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        # import pdb ; pdb.set_trace()
        self.assertEqual(serializer.errors["username"][0].code, "required")
        self.assertEqual(
            serializer.errors["username"][0].title(), "This Field Is Required."
        )
        self.assertEqual(serializer.errors["email"][0].code, "required")
        self.assertEqual(
            serializer.errors["email"][0].title(), "This Field Is Required."
        )

    def test_user_serializer_username_invalid(self):
        payload = {
            "username": "tt",
            "email": "teste@email.com",
            "full_name": "Teste",
            "password": "@Teste123",
        }
        serializer = UserCreateSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        # import pdb ; pdb.set_trace()
        """
        (Pdb) serializer.errors
        {'username': [ErrorDetail(string='Username precisa de no minimo 4 caracteres', code='invalid')]}
        """
        self.assertEqual(
            serializer.errors["username"][0],
            "Username precisa de no minimo 4 caracteres",
        )

    def test_user_serializer_username_invalid(self):
        payload = {
            "username": "tt",
            "email": "teste",
            "full_name": "Teste",
            "password": "@Teste123",
        }
        serializer = UserCreateSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        # import pdb ; pdb.set_trace()
        self.assertEqual(
            serializer.errors["email"][0], "O email não esta num formato valido"
        )

    def test_user_serializer_password_invalid(self):
        payload = {
            "username": "tt",
            "email": "teste",
            "full_name": "Teste",
            "password": "Teste123",
        }
        serializer = UserCreateSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["password"][0], "A senha deve conter carcateres especiais"
        )
