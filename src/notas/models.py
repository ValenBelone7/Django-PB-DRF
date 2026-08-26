from django.conf import settings
from django.db import models


class Bien(models.Model):
    TIPOS = [
        ('DINERO', 'Dinero'),
        ('ARCHIVO', 'Archivo'),
        ('IMAGEN', 'Imagen'),
        ('CONTRASENA', 'Contrasenia'),
        ('DOCUMENTO', 'Documento'),
        ('BITCOIN', 'Bitcoin'),
        ('OTRO', 'Otro'),
    ]

    ESTADOS = [
        ('BLOQUEADO', 'Bloqueado'),
        ('TRANSFERIDO', 'Transferido'),
    ]

    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=12, choices=TIPOS, default='OTRO')
    # 8 decimales para que entre la cantidad de bitcoin (0.05)
    valor = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    archivo = models.FileField(upload_to='bienes/', null=True, blank=True)
    estado = models.CharField(max_length=12, choices=ESTADOS, default='BLOQUEADO')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_transferencia = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Asignacion(models.Model):
    # que heredero recibe que bien y cuanto
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    heredero = models.ForeignKey('users.Heredero', on_delete=models.CASCADE)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.bien.nombre} - {self.heredero.nombre} ({self.porcentaje}%)'
