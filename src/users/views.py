from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Heredero, User
from .serializers import HerederoPublicSerializer, HerederoSerializer, UserSerializer


# ReadOnlyModelViewSet: solo lectura, sin alta/baja/modificación por API
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    @extend_schema(
        summary="Lista los usuarios del sistema",
        description=(
            "Endpoint de solo lectura: sirve para consultar quién es el `propietario` de un "
            "bien o el `usuario` de un heredero. Los usuarios no se crean ni se editan por la "
            "API, se administran desde `/admin/`."
        ),
        responses={
            200: UserSerializer(many=True),
            401: OpenApiResponse(description="Falta el token JWT o es inválido"),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)  # No cambiamos la función interna del list


# ModelViewSet: CRUD completo
class HerederoViewSet(viewsets.ModelViewSet):
    queryset = Heredero.objects.all().select_related("usuario")
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HerederoPublicSerializer
        return HerederoSerializer

    @extend_schema(
        summary="Registra un nuevo heredero",
        description=(
            "Crea un heredero para el usuario `main` indicado por ID. El campo `usuario` es "
            "opcional: se completa cuando el heredero tiene cuenta propia en el sistema."
        ),
        responses={
            201: HerederoSerializer,  # created
            400: OpenApiResponse(description="Error de validación (ej: main inexistente o porcentaje inválido)"),
            401: OpenApiResponse(description="Falta el token JWT o es inválido"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)  # No cambiamos la función interna del create
