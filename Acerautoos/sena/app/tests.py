from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import PerfilUsuario

User = get_user_model()


class PerfilUsuarioModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="juan",
            password="12345678"
        )

        self.perfil = PerfilUsuario.objects.create(
            user=self.user,
            rol="cliente",
            cedula="123456789",
            telefono="3001234567"
        )

    def test_crear_perfil_usuario(self):
        """Verifica que el perfil se cree correctamente."""
        self.assertEqual(self.perfil.user.username, "juan")
        self.assertEqual(self.perfil.rol, "cliente")
        self.assertEqual(self.perfil.cedula, "123456789")
        self.assertEqual(self.perfil.telefono, "3001234567")

    def test_str(self):
        """Verifica el método __str__."""
        self.assertEqual(str(self.perfil), "juan - Cliente")

    def test_rol_por_defecto(self):
        """Verifica que el rol por defecto sea cliente."""
        user2 = User.objects.create_user(
            username="maria",
            password="12345678"
        )

        perfil2 = PerfilUsuario.objects.create(
            user=user2,
            cedula="987654321"
        )

        self.assertEqual(perfil2.rol, "cliente")

    def test_verbose_name(self):
        """Verifica el verbose_name del modelo."""
        self.assertEqual(
            PerfilUsuario._meta.verbose_name,
            "Perfil de Usuario"
        )

    def test_verbose_name_plural(self):
        """Verifica el verbose_name_plural."""
        self.assertEqual(
            PerfilUsuario._meta.verbose_name_plural,
            "Perfiles de Usuarios"
        )

    def test_db_table(self):
        """Verifica el nombre de la tabla."""
        self.assertEqual(
            PerfilUsuario._meta.db_table,
            "perfil_usuario"
        )

    def test_cedula_es_unica(self):
        """Verifica que la cédula sea única."""
        user2 = User.objects.create_user(
            username="pedro",
            password="12345678"
        )

        with self.assertRaises(Exception):
            PerfilUsuario.objects.create(
                user=user2,
                rol="empleado",
                cedula="123456789"
            )