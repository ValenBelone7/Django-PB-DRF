from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Asignacion, Bien
from .serializers import (
    AsignacionPublicSerializer,
    AsignacionSerializer,
    BienPublicSerializer,
    BienSerializer,
)


# ModelViewSet: CRUD completo
class BienViewSet(viewsets.ModelViewSet):
    queryset = Bien.objects.all().select_related("propietario")
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BienPublicSerializer
        return BienSerializer


# ModelViewSet: CRUD completo
class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all().select_related(
        "bien", "heredero", "bien__propietario", "heredero__usuario"
    )
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AsignacionPublicSerializer
        return AsignacionSerializer
