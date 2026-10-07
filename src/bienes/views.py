from drf_spectacular.utils import OpenApiResponse, extend_schema
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

    @extend_schema(
        summary="Registra un nuevo bien digital",
        description=(
            "Crea un bien (dinero, archivo, imagen, contraseña, documento, bitcoin u otro) "
            "a nombre del `propietario` indicado por ID. Si no se envía `estado`, el bien "
            "nace `BLOQUEADO` hasta que se active la herencia. La respuesta devuelve el "
            "`propietario` como ID; para verlo anidado usar `GET /api/bienes/{id}/`."
        ),
        responses={
            201: BienSerializer,  # created
            400: OpenApiResponse(description="Error de validación (ej: tipo inválido o propietario inexistente)"),
            401: OpenApiResponse(description="Falta el token JWT o es inválido"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)  # No cambiamos la función interna del create


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

    @extend_schema(
        summary="Asigna un bien a un heredero",
        description=(
            "Indica qué `porcentaje` de un `bien` recibirá un `heredero` cuando se active la "
            "herencia. Ambos se envían por ID. Un mismo bien puede repartirse entre varios "
            "herederos creando una asignación por cada uno (ej: 50% y 50%)."
        ),
        responses={
            201: AsignacionSerializer,  # created
            400: OpenApiResponse(description="Error de validación (ej: bien o heredero inexistente)"),
            401: OpenApiResponse(description="Falta el token JWT o es inválido"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)  # No cambiamos la función interna del create
