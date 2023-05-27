import unittest

from clases.contactoempresa import ContactoEmpresa

class TestContactoEmpresa(unittest.TestCase):
    def test_crear(self):
        contactoempresa = ContactoEmpresa()
        self.assertEqual(contactoempresa._tipo, "EMPRESA")
        self.assertEqual(contactoempresa._telefono, 678444563)
        self.assertEqual(contactoempresa._fecha_ingreso, "2023-01-01")
        self.assertEqual(contactoempresa._nombre, "Mario S.L.")
        self.assertEqual(contactoempresa._descripcion_empresa, "Empresa \
con 100.000 trabajadores")
        self.assertEqual(contactoempresa._pagina_web, "www.mariosl.com")
    
    def test_str(self):
        contactoempresa = ContactoEmpresa("EMPRESA", 678444653, "2023-01-01", 
        "Mario S.L.", "Empresa con 100.000 trabajadores", "www.mariosl.com")
        self.assertEqual("EMPRESA;678444653;2023-01-01;Mario S.L.;\
Empresa con 100.000 trabajadores;www.mariosl.com", str(contactoempresa))

    def test_igualdad(self):
        self.assertTrue(ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Mario S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
         == ContactoEmpresa("EMPRESA", 678444653, "2023-01-01", 
        "Mario S.L.", "Empresa con 100.000 trabajadores", "www.mariosl.com"))

    def test_no_igualdad(self):
        self.assertFalse(ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Mario.com", "Empresa con 500.000 trabajadores", "www.mariosl.com") 
        == ContactoEmpresa("EMPRESA", 678444653, "2023-01-01", 
        "Mario S.L.", "Empresa con 100.000 trabajadores", "www.mariosl.com"))

    def test_compare_with_others(self):
        self.assertFalse(ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Mario.com", "Empresa con 500.000 trabajadores", "www.mariosl.com")
         == "abc")
        self.assertFalse(ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Mario.com", "Empresa con 500.000 trabajadores", "www.mariosl.com")
          == 7)

