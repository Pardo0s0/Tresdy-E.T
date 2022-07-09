from rest_framework import serializers
from core.models import *
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','categoria','stock','precio','descuento']