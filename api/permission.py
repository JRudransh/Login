from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        try:
            allowed = request.user.id == view.get(request).data['id']
        except Exception as e:
            allowed = e and False
        return bool(request.user.is_authenticated and allowed)
