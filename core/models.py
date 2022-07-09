from distutils.command.upload import upload
from hashlib import blake2b
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCategoria

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descuento = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.nombre+" "+self.codigo