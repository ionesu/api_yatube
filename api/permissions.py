from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user and request.method in permissions.SAFE_METHODS:
            return True
