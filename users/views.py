from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.serializers import UserCreateSerializer
from users.services import UserService


class UserAPIView(APIView):
    service = UserService()

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.service.create_user(serializer.data)

        if user:
            serializer = UserCreateSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"error": "Erro ao criar um usuário"}, status=status.HTTP_400_BAD_REQUEST
        )
