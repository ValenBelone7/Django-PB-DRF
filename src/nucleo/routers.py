from rest_framework.routers import DefaultRouter

from bienes.views import AsignacionViewSet, BienViewSet
from users.views import HerederoViewSet, UserViewSet

router = DefaultRouter()

router.register("usuarios", UserViewSet, basename="usuario")
router.register("herederos", HerederoViewSet, basename="heredero")
router.register("bienes", BienViewSet, basename="bien")
router.register("asignaciones", AsignacionViewSet, basename="asignacion")
