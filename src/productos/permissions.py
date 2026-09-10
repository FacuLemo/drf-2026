"""
from rest_framework import permissions


class GroupEditProductoPermission(permissions.BasePermission):
    #Permisson custom para permitir acceso si es staff
    def has_permission(self, request, view):
        #logica
        return request.user.is_staff
"""