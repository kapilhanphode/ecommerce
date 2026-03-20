from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "admin"


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "vendor"


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "customer"