from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Пермишен проверяет, является ли пользователь владельцем или админом
    """

    def has_permission(self, request, view):
        if request.user in view.get_queryset() or request.user.is_superuser:
            return True
        else:
            return False


class IsActive(BasePermission):
    """
    Пермишен проверяет, активен ли пользователь
    """
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False
