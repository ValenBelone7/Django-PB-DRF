from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [
        ('MAIN', 'Main'),
        ('HEREDERO', 'Heredero'),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default='MAIN')

    def __str__(self):
        return self.username


class Heredero(models.Model):
    # el Main que lo designo
    main = models.ForeignKey(User, on_delete=models.CASCADE, related_name='herederos')
    # la cuenta del heredero (puede no tener todavia)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class CheckIn(models.Model):
    ESTADOS = [
        ('ACTIVO', 'Activo'),
        ('ADVERTENCIA', 'Advertencia'),
        ('VENCIDO', 'Vencido'),
        ('HERENCIA_ACTIVADA', 'Herencia activada'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    ultima_confirmacion = models.DateTimeField(auto_now_add=True)
    periodo_dias = models.IntegerField(default=30)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVO')

    def __str__(self):
        return f'Check-in de {self.usuario.username}'


class Herencia(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ACTIVA', 'Activa'),
        ('PROCESADA', 'Procesada'),
    ]

    main = models.OneToOneField(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='PENDIENTE')
    fecha_activacion = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Herencia de {self.main.username}'
