import unittest

from clases.validator import Validator

class TestValidator(unittest.TestCase):
    def test_expresion_telefono(self):
        telefono = 949494949
        self.assertTrue(telefono)
    
    def test_no_expresion_telefono(self):
        telefono1 = 949494
        telefono2 = "b"
        self.assertFalse(telefono1) #NÚMERO DE MENOS DE 9 DÍGITOS
        self.assertFalse(telefono2) 

    def test_expresion_nombre(self):
        nombre1 = "MARIO PÉREZ"
        nombre2 = "MARTA SÁNCHEZ-ARJONA"
        self.assertTrue(nombre1)
        self.assertTrue(nombre2)

    def test_no_expresion_nombre(self):
        nombre1 = 9878695
        nombre2 = "MARIO.GLD"
        self.assertFalse(nombre1)
        self.assertFalse(nombre2) #CONTIENE CARACTÉRES DISTINTOS A 
                                  #LETRAS Y GUIONES

    def test_expresion_cumpleanios(self):
        cumpleanios1 = "2000-01-01"
        self.assertTrue(cumpleanios1)

    def test_no_expresion_cumpleanios(self):
        cumpleanios1 = "02-01-01"
        cumpleanios2 = "2000/01/01"
        cumpleanios3 = 3469858
        self.assertFalse(cumpleanios1) #EL AÑO CONTIENE LOS 4 DÍGITOS
        self.assertFalse(cumpleanios2) #PARA SEPARAR SOLO SON VALIDADOS
                                       # LOS GUIONES
        self.assertFalse(cumpleanios3)

    def test_expresion_nombre_empresa(self):
        nombre = "ejemplo.com"
        self.assertTrue(nombre)
    
    def test_no_expresion_nombre_empresa(self):
        nombre1 = "MA380757"
        nombre2 = 343563
        self.assertFalse(nombre1)
        self.assertFalse(nombre2)

        

