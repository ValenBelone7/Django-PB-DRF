"""
from rest_framework import permissions


class EsPropietarioOSoloLectura(permissions.BasePermission):
    # Permiso a nivel de objeto: cualquier autenticado puede leer,
    # pero solo el propietario del bien puede editarlo o borrarlo.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.propietario == request.user
"""
