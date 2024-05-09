from rest_framework.permissions import BasePermission


class IsOwnerOrganization(BasePermission):
    """
    Пермишен проверяет, является ли пользователь владельцем организации или админом
    """

    def has_permission(self, request, view):
        for obj in view.get_queryset():
            if request.user == obj.user or request.user.is_superuser:
                return True
            return False


class IsOwnerProduct(BasePermission):
    """
    Пермишен проверяет, является ли пользователь владельцем товара или админом
    """
    def has_permission(self, request, view):
        for obj in view.get_queryset():
            if request.user == obj.organization.user or request.user.is_superuser:
                return True
            return False
