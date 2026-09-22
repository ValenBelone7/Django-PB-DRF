from rest_framework import generics

from .models import Asignacion, Bien
from .serializers import (
    AsignacionPublicSerializer,
    AsignacionSerializer,
    BienPublicSerializer,
    BienSerializer,
)


class BienesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bien.objects.all().select_related("propietario")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BienPublicSerializer
        return BienSerializer


class BienDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bien.objects.all()
    serializer_class = BienSerializer


class AsignacionesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Asignacion.objects.all().select_related(
        "bien", "heredero", "bien__propietario", "heredero__usuario"
    )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AsignacionPublicSerializer
        return AsignacionSerializer


class AsignacionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
