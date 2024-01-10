from django.test import TestCase
from users.models import User
from users.choices import UserTypeChoice


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            username="teste",
            email="teste@email.com",
        )
        self.assertEqual(user.username, "teste")
        self.assertEqual(user.email, "teste@email.com")
        self.assertEqual(user.type, UserTypeChoice.STUDENT)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create(
            username="teste",
            email="teste@email.com",
            is_superuser=True,
        )
        self.assertEqual(user.username, "teste")
        self.assertEqual(user.email, "teste@email.com")
        self.assertEqual(user.type, UserTypeChoice.STUDENT)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)

    def test_user_str(self):
        user = User.objects.create(
            username="teste",
            email="teste@email.com",
            is_superuser=True,
        )
        self.assertEqual(user.__str__(), f"{user.id} - {user.username}")
