from clases.contacto import Contacto

class ContactoEmpresa(Contacto):
    def __init__(self, tipo:str, telefono, nombre:str, fecha_ingreso, 
    descripcion_empresa:str, pagina_web:str):
        super().__init__(tipo, telefono, nombre, fecha_ingreso)
        self._descripcion_empresa = descripcion_empresa
        self._pagina_web = pagina_web

    def __str__(self):
        return f"{self._tipo};{self._telefono};{self._nombre};\
{self._fecha_ingreso};{self._descripcion_empresa};{self._pagina_web}"

    def __repr__(self):
        return f"TIPO: {self._tipo}\nTELÉFONO: {self._telefono}\n\
NOMBRE: {self._nombre}\nFECHA DE INGRESO: {self._fecha_ingreso}\n\
DESCRIPCIPCIÓN DE LA EMPRESA: {self._descripcion_empresa}\n\
PÁGINA WEB: {self._pagina_web}"

    def __eq__(self, other):
        if isinstance(other, Contacto):
            return self._nombre == other._nombre
        return False
