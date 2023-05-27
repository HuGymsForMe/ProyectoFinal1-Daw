import unittest

from clases.agenda import Agenda

class TestAgenda(unittest.TestCase):
    def test_add_contacto_personal(self):
        contacto1 = ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Mario", "2000-01-01")
        contacto2 = ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Pedro", "2000-01-01")
        contacto3 = ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Pepe", "2000-01-01")
        contacto4 = ContactoPersona("PERSONAL", 678444653, "2023-01-01", 
        "Marta", "2000-01-01")

        arraycontactos = [contacto1, contacto2, contacto3]
        self.assertEqual(contacto1 in arraycontactos, 
        [contacto1, contacto2, contacto3])
        self.asssertEqual(contacto4 in arraycontactos, 
        [contacto1, contacto2, contacto3, contacto4])

    def test_add_contacto_empresa(self):
        contacto1 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Mario S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
        contacto2 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Pepe S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
        contacto3 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Juan S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
        contacto4 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Marta S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")

        arraycontactos = [contacto1, contacto2, contacto3]
        self.assertEqual(contacto1 in arraycontactos, 
        [contacto1, contacto2, contacto3])
        self.asssertEqual(contacto4 in arraycontactos, 
        [contacto1, contacto2, contacto3, contacto4])

    def test_del_busqueda_contacto_empresa(self): 
        '''
        Vale para borrar, buscar y existe
        '''
        contacto1 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Mario S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
        contacto2 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Pepe S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
        contacto3 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Juan S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
        contacto4 = ContactoEmpresa("EMPRESA", 678444653, "2023-03-07", 
        "Marta S.L.", "Empresa con 500.000 trabajadores", "www.mariosl.com")
        contacto_buscado1 = "Mario S.L"
        contacto_buscado2 = "Mario"

        arraycontacto_buscado = [contacto1, contacto2, contacto3, contacto4]
        self.asssertTrue(contacto_buscado1 in arraydefecto)
        self.assertFalse(contacto_buscado2 in arraydefecto)


