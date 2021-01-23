from rest_framework import permissions


class IsTeacherOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user


class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user.is_teacher() | request.user.is_admin()


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        # Write permissions are only allowed to the author of a post
        return request.user.is_admin()
