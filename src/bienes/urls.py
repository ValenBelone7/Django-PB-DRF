from django.urls import path

from .views import (
    AsignacionDetailAPIView,
    AsignacionesListCreateAPIView,
    BienDetailAPIView,
    BienesListCreateAPIView,
)

urlpatterns = [
    path("bienes/", BienesListCreateAPIView.as_view(), name="bienes_api"),
    path("bienes/<int:pk>/", BienDetailAPIView.as_view(), name="bien_detail_api"),
    path("asignaciones/", AsignacionesListCreateAPIView.as_view(), name="asignaciones_api"),
    path(
        "asignaciones/<int:pk>/",
        AsignacionDetailAPIView.as_view(),
        name="asignacion_detail_api",
    ),
]
