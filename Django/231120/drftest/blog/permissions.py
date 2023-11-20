from rest_framework import permissions


class IsUserOrRestricted(permissions.BasePermission):
    def has_permission(self, request, view):
        # 현재 유저가 인증받은 유저인 경우에만 허용
        if request.user and request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        # 'GET', 'HEAD', 'OPTIONS' - 모두 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 'PUT' 'DELETE' - 현재 유저가 obj(post글)의 작성자 본인 경우에만 허용
        return obj.author == request.user