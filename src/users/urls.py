from django.urls import path

from .views import heredero_detail, herederos

urlpatterns = [
    path("herederos/", herederos, name="herederos_api"),
    path("herederos/<int:pk>/", heredero_detail, name="heredero_detail_api"),
]
