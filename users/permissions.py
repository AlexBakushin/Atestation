from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Пермишен проверяет, является ли пользователь владельцем привычки или админом
    """

    def has_permission(self, request, view):
        for obj in view.get_queryset():
            if request.user == obj or request.user.is_superuser:
                return True
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj == request.user
