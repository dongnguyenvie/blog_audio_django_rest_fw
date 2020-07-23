from rest_framework.permissions import BasePermission

class IsUserPermissionsView(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in ('POST') or
            request.user and
            request.user.is_authenticated
        )