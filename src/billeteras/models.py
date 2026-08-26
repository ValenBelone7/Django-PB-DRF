from django.conf import settings
from django.db import models


class Billetera(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def __str__(self):
        return f'Billetera de {self.usuario.username}'


class Transaccion(models.Model):
    TIPOS = [
        ('DEPOSITO', 'Deposito'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('HERENCIA', 'Herencia'),
    ]

    # si no tiene origen es un deposito, si no tiene destino es un retiro
    origen = models.ForeignKey(
        Billetera, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='enviadas',
    )
    destino = models.ForeignKey(
        Billetera, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='recibidas',
    )
    monto = models.DecimalField(max_digits=14, decimal_places=2)
    tipo = models.CharField(max_length=14, choices=TIPOS, default='TRANSFERENCIA')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} de ${self.monto}'
