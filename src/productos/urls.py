from django.urls import path

from .views import ArticulosDetailAPIView, ArticulosListCreateAPIView, proveedor

urlpatterns = [
    path("articulos/", ArticulosListCreateAPIView.as_view(), name="articulos_api"),
    path(
        "articulos/<int:pk>/",
        ArticulosDetailAPIView.as_view(),
        name="articulo_detail_api",
    ),
    path("proveedor/", proveedor, name="proveedor_api"),
]
