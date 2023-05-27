import unittest

from clases.contacto import Contacto

class TestContacto(unittest.TestCase):
    def test_crear(self):
        contacto = Contacto()
        self.assertEqual(contacto._tipo, "PERSONAL")
        self.assertEqual(contacto._telefono, 949356475)
        self.assertEqual(contacto._fecha_ingreso, "2023-01-01")
        self.assertEqual(contacto._nombre, "Pepe")

    def test_str(self):
        contacto = Contacto("PERSONAL", 949356374, "2023-01-01" "Pepe")
        self.assertEqual("PERSONAL;949356475;2023-01-01;Pepe", str(contacto))
