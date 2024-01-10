from django.test import TestCase
from users.models import UserConfirmation, User


class UserConfirmationModelTestCase(TestCase):
    def test_create_user_confirmation(self):
        user = User.objects.create(
            username="teste",
            email="teste@email.com",
        )
        user_confirmation = UserConfirmation.objects.create(
            user=user,
        )
        self.assertEqual(user_confirmation.user, user)
        self.assertFalse(user_confirmation.is_confirmed)

    def test_user_confirmation_str(self):
        user = User.objects.create(
            username="teste",
            email="teste@email.com",
            full_name="teste teste",
        )
        user_confirmation = UserConfirmation.objects.create(
            user=user,
            code="123456",
        )
        self.assertEqual(
            user_confirmation.__str__(),
            f"{user_confirmation.id} - {user_confirmation.code} - {user_confirmation.user.full_name}",
        )
