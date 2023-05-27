from abc import ABC, abstractmethod

class Contacto(ABC):
    def __init__(self, tipo:str, telefono:int, nombre:str, fecha_ingreso 
    = "2023-01-01"):
        '''
        AÑADIMOS EL ATRIBUTO TIPO QUE PUEDA HABER DOS CONTACTOS CON EL
        MISMO NOMBRE PERO DE DISTINTO TIPO
        '''
        self._tipo = tipo 
        self._telefono = telefono
        self._nombre = nombre
        self._fecha_ingreso = fecha_ingreso
    
    def __str__(self):
        return f"{self._tipo};{self._telefono};{self._fecha_ingreso}\
;{self._nombre}"

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass