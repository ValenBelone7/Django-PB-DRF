from rest_framework import serializers

from users.serializers import HerederoPublicSerializer, UserSerializer

from .models import Asignacion, Bien


class BienPublicSerializer(serializers.ModelSerializer):
    propietario = UserSerializer(read_only=True)  # Many=True si fuera relacion Muchos Muchos

    class Meta:
        model = Bien
        fields = [  # noqa: RUF012
            "id",
            "nombre",
            "descripcion",
            "tipo",
            "estado",
            "fecha_creacion",
            "propietario",  # Nested Field
        ]
        read_only_fields = ["id", "fecha_creacion"]  # noqa: RUF012


class BienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bien
        fields = [  # noqa: RUF012
            "id",
            "nombre",
            "descripcion",
            "tipo",
            "valor",
            "archivo",
            "estado",
            "propietario",  # Primary Key Related Field
            "fecha_creacion",
            "fecha_transferencia",
        ]
        read_only_fields = ["id", "fecha_creacion"]  # noqa: RUF012


class AsignacionPublicSerializer(serializers.ModelSerializer):
    bien = BienPublicSerializer(read_only=True)  # Nested Field
    heredero = HerederoPublicSerializer(read_only=True)  # Nested Field

    class Meta:
        model = Asignacion
        fields = [  # noqa: RUF012
            "id",
            "bien",  # Nested Field
            "heredero",  # Nested Field
            "porcentaje",
            "fecha_asignacion",
        ]
        read_only_fields = ["id", "fecha_asignacion"]  # noqa: RUF012


class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = [  # noqa: RUF012
            "id",
            "bien",  # Primary Key Related Field
            "heredero",  # Primary Key Related Field
            "porcentaje",
            "fecha_asignacion",
        ]
        read_only_fields = ["id", "fecha_asignacion"]  # noqa: RUF012
