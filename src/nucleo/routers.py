from rest_framework.routers import DefaultRouter

from users.views import HerederoViewSet, UserViewSet

router = DefaultRouter()

router.register("usuarios", UserViewSet, basename="usuario")
router.register("herederos", HerederoViewSet, basename="heredero")
