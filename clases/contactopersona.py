from clases.contacto import Contacto

class ContactoPersona(Contacto):
    def __init__(self, tipo:str, telefono, nombre:str, fecha_ingreso, 
    cumpleanios:str):
        super().__init__(tipo, telefono, nombre, fecha_ingreso)
        self._cumpleanios = cumpleanios

    def __str__(self):
        return f"{self._tipo};{self._telefono};{self._nombre}\
;{self._fecha_ingreso};{self._cumpleanios}"

    def __repr__(self):
        return f"TIPO: {self._tipo}\nTELÉFONO: {self._telefono}\n\
NOMBRE: {self._nombre}\nFECHA DE INGRESO: {self._fecha_ingreso}\n\
FECHA DE NACIMIENTO: {self._cumpleanios}"

    def __eq__(self, other):
        if isinstance(other, Contacto):
            return self._nombre == other._nombre
        return False