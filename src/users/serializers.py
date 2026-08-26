from rest_framework import serializers
from .models import CheckIn, Heredero, Herencia, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'role']
        read_only_fields = ['id']


class HerederoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heredero
        fields = ['id', 'main', 'usuario', 'nombre', 'porcentaje', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = [
            'id',
            'usuario',
            'ultima_confirmacion',
            'periodo_dias',
            'fecha_vencimiento',
            'estado',
        ]
        read_only_fields = ['id', 'ultima_confirmacion']


class HerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herencia
        fields = [
            'id',
            'main',
            'estado',
            'fecha_activacion',
            'fecha_finalizacion',
        ]
        read_only_fields = ['id']
