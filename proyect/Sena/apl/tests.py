from django.test import TestCase
from apl.models import Categoria

class PruebaBasica(TestCase):
    def test_verificar_entorno(self):
        #Una prueba simple para validad que CI/CD funciona
        self.assertEqual(1+1, 2)
        
    def test_crear_categoria(self):
        #Prueba básica de base de datos en memoria
        #Las consultas e inserciones van Dentro de las funciones
        Categoria.objects.create(nombre="Frijol")
        consulta = Categoria.objects.filter(nombre="Frijol")
        self.assertTrue(consulta.exists())