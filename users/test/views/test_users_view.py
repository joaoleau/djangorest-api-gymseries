from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("users")  #'users' == name da url

    def test_create_user(self):
        payload = {
            "username": "teste",
            "email": "teste@email.com",
            "full_name": "Teste",
            "password": "@Teste123",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(email=payload.get("email")).exists())

    def test_create_user_invalid_payload(self):
        payload = {
            "username": "teste",
            "email": "teste@email.com",
            "full_name": "Teste",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
