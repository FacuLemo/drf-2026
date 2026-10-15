from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Articulo, Proveedor

# Create your tests here.


class ArticuloTests(APITestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(nombre="arcor", telefono="35834123")
        self.usuario = User.objects.create_user("pepe", password="1234")
        self.articulo = Articulo.objects.create(
            nombre="Caramelo", precio=123, stock=999, proveedor=self.proveedor
        )
        self.url = "/api/articulos/"

    def test_list_articulos_sin_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_articulo_sin_auth(self):
        data = {
            "nombre": "Caramelo",
            "precio": 123,
            "stock": 999,
            "proveedor": self.proveedor,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_articulo_con_auth(self):
        # autenticar primero
        self.client.login(username="pepe", password="1234")
        data = {
            "nombre": "Caramelo 22",
            "precio": 123,
            "stock": 999,
            "proveedor": self.proveedor.id,
        }
        response = self.client.post(self.url, data)
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
