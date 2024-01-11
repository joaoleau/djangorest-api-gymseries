from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.serializers import (
    UserCreateSerializer,
    UserConfirmationRequestCodeSerializer,
    UserConfirmationRequestEmailSerializer,
)
from users.services import UserService, UserConfirmationService
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


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


class LoginView(TokenObtainPairView):
    service = UserService()

    def post(self, request, *args, **kwargs):
        user = self.service.get_user(
            username=request.data.get("username"), is_active=True
        )

        response = super().post(request, *args, **kwargs)

        response.data["user"] = {"username": user.username, "id": user.id}

        return response


class UserConfirmationRequestEmailView(APIView):
    serializer_class = UserConfirmationRequestEmailSerializer
    service = UserConfirmationService()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_confirmation = self.service.create(**serializer.validated_data)
        return Response(
            {"code": user_confirmation.code}, status=status.HTTP_201_CREATED
        )


class UserConfirmationRequestCodeView(APIView):
    serializer_class = UserConfirmationRequestCodeSerializer
    service = UserConfirmationService()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        is_active = self.service.verify_code(**serializer.validated_data)

        if is_active:
            return Response(
                {"message": "Usuario foi confirmado com sucesso"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": "Codigo nao existe"}, status=status.HTTP_400_BAD_REQUEST
        )
