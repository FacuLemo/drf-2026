from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .models import Articulo, Proveedor
from .serializers import ArticuloSerializer, ProveedorSerializer, ArticuloPublicSerializer

# Objeto Python -> No se envia en Response
# hay que Serializarlo
# Objeto de Python -> JSON: JavaScript Object Notation
# Articulo -> {"nombre": "lata de atún", "precio":1500, "timestamps"}

# [{},{},{},{}]

# APIS RESTFUL

# GET /ARTICULO
# POST /ARTICULO


@api_view(["GET", "POST"])
def articulos(request):
    if request.method == "GET":
        articulos = Articulo.objects.all().select_related("proveedor") #Evitar el N+1 con select_related
        #Si tuviera relación muchos muchos, uso también prefetch_related("categoria") por ejemplo
        serializer = ArticuloPublicSerializer(articulos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Articulo creado"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"mensaje": "No se creó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# PUT ->   editar CUAL
# Delete-> borrar QUE


# id == pk -> Primary Key
@api_view(["GET", "PUT", "DELETE"])
def articulos_detail(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    
    if request.method == "GET":
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = ArticuloSerializer(articulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Articulo Actualizado"}, status=status.HTTP_200_OK
            )
        return Response(
            {"mensaje": "No se Actualizó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if request.method == "DELETE":
        articulo.delete()
        return Response(
            {"mensaje": "Articulo Borrado"},
            status=status.HTTP_200_OK,
        )


#----------------------


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