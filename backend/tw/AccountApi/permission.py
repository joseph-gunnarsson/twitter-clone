from rest_framework.permissions import BasePermission


class isAuthUser(BasePermission):
    def  has_permission(self, request, view):