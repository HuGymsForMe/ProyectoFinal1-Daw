import unittest

from clases.contactopersona import ContactoPersona

class TestContactoPersona(unittest.TestCase):
    def test_crear(self):
        contactopersonal = ContactoPersona()
        self.assertEqual(contactopersonal._tipo, "PERSONAL")
        self.assertEqual(contactopersonal._telefono, 949345678)
        self.assertEqual(contactopersonal._fecha_ingreso, "2023-01-01")
        self.assertEqual(contactopersonal._nombre, "Francisco Pérez")
        self.assertEqual(contactopersonal._cumpleanios, "2004-05-06")

    def test_str(self):
        contactopersonal = Contacto("PERSONAL", 949345678, "2023-01-01", 
        "Francisco", "2004-05-06")
        self.assertEqual("PERSONAL;949345678;2023-01-01;Francisco;\
2004-05-06", str(contactopersonal))

    def test_igualdad(self):
        self.assertTrue(ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Mario", "2000-01-01") == ContactoPersona("PERSONAL", 666666666,
         "2023-07-04", "Mario", "2000-01-01"))

    def test_no_igualdad(self):
        self.assertFalse(ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Mario", "2000-01-01") == ContactoPersona("PERSONAL", 678444653, 
        "2023-01-01", "Pepe", "2000-01-01"))

    def test_compare_with_others(self):
        self.assertFalse(ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Mario", "2000-01-01") == "abc")
        self.assertFalse(ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Mario", "2000-01-01")  == 7)