from rest_framework.permissions import BasePermission
from users.models import UserRole


class IsActive(BasePermission):
    """
    Настройка права доступа, чтобы только активные сотрудники имели доступ к API.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRole.ADMIN


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
