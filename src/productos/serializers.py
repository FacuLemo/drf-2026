from rest_framework import serializers

from .models import Articulo, Proveedor

# Serializer:
# "Traductor" del ORM hacia un body JSON de la api y viceversa
# También se encarga de validar datos, y dar acceso a otras utilidades del orm como el .save()


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"
        read_only_fields = ["id"]  # noqa: RUF012


class ArticuloPublicSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True) #Many=True si fuera relacion Muchos Muchos

    class Meta:
        model = Articulo
        fields = [  # noqa: RUF012
            "id",
            "nombre",
            "precio",
            "proveedor",  # Nested Field
        ]
        read_only_fields = ["id", "timestamp"]  # noqa: RUF012


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = [  # noqa: RUF012
            "id",
            "nombre",
            "precio",
            "stock",
            "proveedor",  # Primary Key Related Field
            "timestamp",
        ]
        read_only_fields = ["id", "timestamp"]  # noqa: RUF012
