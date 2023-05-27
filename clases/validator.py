import abc
import re

class Validator:
    @staticmethod
    def expresion_telefono(telefono):
        expresion_telefono = r"^\d{9}$"
        verdad = True
        while verdad:
            if re.match(expresion_telefono, str(telefono)):
                return telefono
            else:
                verdad = False
                  
    @staticmethod
    def expresion_nombre(nombre_personal):
        expresion_nombre = r'^[a-zA-Z|áéíóúÁÉÍÓÚüÜñÑ | ]+$'
        verdad = True
        while verdad:
            if re.match(expresion_nombre, nombre_personal, re.UNICODE):
                return nombre_personal
            else:
                verdad = False

    @staticmethod
    def expresion_cumpleanios(cumpleanios):
        expresion_cumpleanios = r'^\d{4}-(0?[1-9]|1[0-2])-(0?[1-9]|[12]\d|3[01])$'
        verdad = True
        while verdad:
            if re.match (expresion_cumpleanios, cumpleanios):
                return cumpleanios
            else: 
                verdad = False

    @staticmethod
    def expresion_nombre_empresa(nombre_empresa):
        expresion_nombre_empresa = r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s.\-\'!? | ]+$'
        verdad = True
        while verdad:
            if re.match (expresion_nombre_empresa, nombre_empresa):
                return nombre_empresa
            else: 
                verdad = False
