from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Articulo, Proveedor
from .serializers import (
    ArticuloPublicSerializer,
    ArticuloSerializer,
    ProveedorSerializer,
)

# Objeto Python -> No se envia en Response
# hay que Serializarlo
# Objeto de Python -> JSON: JavaScript Object Notation
# Articulo -> {"nombre": "lata de atún", "precio":1500, "timestamps"}

# [{},{},{},{}]

# APIS RESTFUL

# GET /ARTICULO
# POST /ARTICULO

# -------------------------------------------
# MIGRACION A VISTAS BASADAS EN CLASES DE DRF:

# Tenemos las clases:
# APIView
# Generics de APIView
# Concrete Generic APIView

# Las dos últimas usan un léxico específico:
# List -> GET all
# Create -> POST
# Retrieve -> GET by id/pk
# Update -> PUT
# Destroy -> Delete


# Concrete generic
class ArticulosListCreateAPIView(generics.ListCreateAPIView):
    queryset = Articulo.objects.all().select_related("proveedor")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ArticuloPublicSerializer
        else:
            return ArticuloSerializer


# Generic APIView
# class ArticulosGenericAPIView(
#     mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
# ):
#     queryset = Articulo.objects.all().select_related("proveedor")

#     def get_serializer_class(self):
#         if self.request.method == "GET":
#             return ArticuloPublicSerializer
#         else:
#             return ArticuloSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# APIView común (no muy diferente a las funciones)
# class ArticulosAPIView(APIView):
#     def get(self, request):
#         articulos = Articulo.objects.all().select_related("proveedor")
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = ArticuloSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"mensaje": "Articulo creado"}, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST,
#         )


# Concrete generic
class ArticulosDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


# Generic APIView
# class ArticulosDetailGenericAPIView(
#     mixins.DestroyModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Articulo.objects.all()
#     serializer_class = ArticuloSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# APIVIEW común
# class ArticuloDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Articulo, pk=pk)

#     def get(self, request, pk):
#         articulo = self.get_object(pk)
#         serializer = ArticuloSerializer(articulo)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         articulo = self.get_object(pk)
#         serializer = ArticuloSerializer(articulo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"mensaje": "Articulo Actualizado"}, status=status.HTTP_200_OK
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST,
#         )

#     def delete(self, request, pk):
#         articulo = self.get_object(pk)
#         articulo.delete()
#         return Response(
#             {"mensaje": "Articulo Borrado"},
#             status=status.HTTP_200_OK,
#         )


# ----------------------------------


@api_view(["GET", "POST"])
def proveedor(request):
    if request.method == "GET":
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Proveedor creado"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"mensaje": "No se creó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )
