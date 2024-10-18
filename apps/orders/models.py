from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('E', 'En espera'),
        ('P', 'En preparación'),
        ('T', 'Terminado')
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observaciones = models.TextField(null=True, blank=True)
    para_llevar = models.BooleanField(default=False)
    estado = models.CharField(max_length=1, choices=ESTADOS_PEDIDO, default='E')
