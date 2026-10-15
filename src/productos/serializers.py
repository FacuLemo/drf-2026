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
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Articulo
        fields = [
            "id",
            "nombre",
            "stock",
            "precio",
            "proveedor",  # Nested Field
            "timestamp",
        ]
        read_only_fields = ["id", "timestamp"]


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
