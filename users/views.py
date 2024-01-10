from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserCreateSerializer

class UserAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)