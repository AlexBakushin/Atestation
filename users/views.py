from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.serliazers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from users.permissions import IsOwner, IsActive


class UserViewSet(viewsets.ModelViewSet):
    """
    Эндпоинт для работы с пользователями
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        """
        При создании присваивается пароль
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        """
        Ограничения режимами доступа
        """
        if self.action == 'create':
            self.permission_classes = []
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsActive, IsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsActive, IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsActive, IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsActive, IsOwner]

        return [permission() for permission in self.permission_classes]
