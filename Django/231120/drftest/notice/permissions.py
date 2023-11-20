from rest_framework import permissions


class IsLoginOrRestricted(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 'GET', 'HEAD', 'OPTIONS'
        if request.method in permissions.SAFE_METHODS:
            return True

        # 'PUT' 'DELETE'
        return obj.author == request.user
