from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Heredero, User
from .serializers import HerederoPublicSerializer, HerederoSerializer, UserSerializer


# ReadOnlyModelViewSet: solo lectura, sin alta/baja/modificación por API
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # noqa: RUF012


# ModelViewSet: CRUD completo
class HerederoViewSet(viewsets.ModelViewSet):
    queryset = Heredero.objects.all().select_related("usuario")
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HerederoPublicSerializer
        return HerederoSerializer
