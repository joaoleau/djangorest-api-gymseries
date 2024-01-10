from django.test import TestCase
from users.serializers import UserCreateSerializer

class UserCreateSerializerTestCase(TestCase):
    def test_user_serializer_valid(self):
        payload = {
            "username":"teste",
            "email":"teste@email.com",
            "full_name":"Teste",
            "password":"@Teste123",
        }
        serializer = UserCreateSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
    
    def test_user_serializer_invalid(self):
        payload = {
            "full_name":"Teste",
            "password":"@Teste123",
        }
        serializer = UserCreateSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        # import pdb ; pdb.set_trace()
        self.assertEqual(serializer.errors["username"][0].code, "required")
        self.assertEqual(serializer.errors["username"][0].title(), "This Field Is Required.")
        self.assertEqual(serializer.errors["email"][0].code, "required")
        self.assertEqual(serializer.errors["email"][0].title(), "This Field Is Required.")