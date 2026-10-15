from django.contrib import admin

from .models import Articulo, Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "telefono")


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock", "proveedor", "timestamp")
    list_filter = ("proveedor",)
    search_fields = ("nombre",)