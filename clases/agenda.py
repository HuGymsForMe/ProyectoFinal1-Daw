import os

from clases.contactoempresa import ContactoEmpresa
from clases.contactopersona import ContactoPersona

class Agenda:
    '''
    HE CREADO EL FICHERO AGENDA.CSV PARA QUE ALMACENE INDISTINTAMENTE
    CONTACTOSDE PERSONA Y DE EMPRESA Y LUEGO CONTACTO_PERSONA.CSV Y 
    CONTACTO_EMPRESA.CSV PARA HACER UNA BASE DE DATOS CON DOS TABLAS 
    UNA QUE ALMACENE LOS CONTACTOS PERSONALES Y OTRA LOS CONTACTOS DE
    EMPRESA
    '''
    class CamposFicheroCsv:
        TIPO = 0
        TELEFONO = 1
        NOMBRE = 2
        FECHA_INGRESO = 3
        DESCRIPCION_EMPRESA = CUMPLEANIOS = 4
        PAGINA_WEB = 5

        @staticmethod
        def opciones():
            return range(Agenda.CamposFicheroCsv.TIPO,
                        Agenda.CamposFicheroCsv.PAGINA_WEB+1)
    
    def __init__(self):
        self._contactos = []
        self.RUTA_FICHEROS = os.path.abspath('../proyecto\
_final_programacion/files')
        self.FICHERO_PERSONAL = "PERSONAL"
        self.FICHERO_EMPRESA = "EMPRESA"

    @property
    def contactos(self):
        return self._contactos

    def cargar_ficheros(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'agenda.csv'), 'r', 
        encoding='UTF-8') as fichero_agenda:
            lineas = fichero_agenda.readlines()
            for linea in lineas:
                datos = linea.split(';')
                tipo = str(datos[self.CamposFicheroCsv.TIPO].strip())
                telefono = str(datos[self.CamposFicheroCsv.TELEFONO].strip())
                nombre = str(datos[self.CamposFicheroCsv.NOMBRE].strip())
                fecha_ingreso = str(datos[self.CamposFicheroCsv.FECHA_INGRESO]
                .strip())
                if tipo == self.FICHERO_PERSONAL:
                    cumpleanios = str(datos[self.CamposFicheroCsv.CUMPLEANIOS]
                    .strip())
                    nuevo_contacto_personal = ContactoPersona(tipo, telefono,
                    nombre, fecha_ingreso, cumpleanios)
                    self._contactos.append(nuevo_contacto_personal)
                elif tipo == self.FICHERO_EMPRESA:
                    descripcion_empresa = str(datos[self.CamposFicheroCsv.
                    DESCRIPCION_EMPRESA].strip())
                    pagina_web = str(datos[self.CamposFicheroCsv.PAGINA_WEB]
                    .strip())
                    nuevo_contacto_empresa = ContactoEmpresa(tipo, telefono,
                    nombre, fecha_ingreso, descripcion_empresa, pagina_web)
                    self._contactos.append(nuevo_contacto_empresa)

    def _add_contacto_personal(self, contacto:ContactoPersona):
        if (isinstance(contacto, ContactoPersona) and contacto 
        not in self._contactos):
            self._contactos.append(contacto)

    def _add_contacto_empresa(self, contacto: ContactoEmpresa):
        if (isinstance(contacto, ContactoEmpresa) and contacto 
        not in self._contactos):
            self._contactos.append(contacto)

    def del_contacto(self, contacto_buscado:str):
        for contacto in self._contactos:
            if contacto._nombre == contacto_buscado:
                self._contactos.remove(contacto)
                return True
        return False

    def busqueda_contacto(self, nombre:str) -> bool:
        '''
        Vale tanto para busqueda contacto como para existe contacto
        '''
        for contacto in self._contactos:
            if contacto._nombre == nombre:
                return True
        return False

    def sobreescribir_ficheros(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'agenda.csv'), 'w', 
        encoding="UTF-8") as fichero_agenda:
            for elemento in self._contactos:
                fichero_agenda.write(str(elemento) + '\n')
        
        with open(os.path.join(self.RUTA_FICHEROS, 
        'contactos_empresa.csv'), 'w', encoding="UTF-8") as fichero_empresa:
            for elemento in self._contactos:
                if elemento._tipo == self.FICHERO_EMPRESA:
                    fichero_empresa.write(str(elemento) + '\n')
        
        with open(os.path.join(self.RUTA_FICHEROS, 
        'contactos_persona.csv'), 'w', encoding="UTF-8") as fichero_persona:
            for elemento in self._contactos:
                if elemento._tipo == self.FICHERO_PERSONAL:
                    fichero_persona.write(str(elemento) + '\n')

