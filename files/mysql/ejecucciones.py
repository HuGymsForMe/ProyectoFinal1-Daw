import os

import mysql.connector

from conexion_bbdd import conexion

class Ejecuccion:
    class ConstantesCampos:
        TELEFONO = 1
        NOMBRE = 2
        FECHA_INGRESO = 3
        DESCRIPCION_EMPRESA = 4
        CUMPLEANIOS = 4
        PAGINA_WEB = 5
        
    def __init__(self):
        self.cnx = conexion()
        self.RUTA_FICHEROS = os.path.abspath('../proyecto\
_final_programacion/files')
        self.DELETE_PREVIO_EMPRESA = f"TRUNCATE TABLE contactos_empresa;"
        self.DELETE_PREVIO_PERSONA = f"TRUNCATE TABLE contactos_persona;"



        @staticmethod
        def opciones():
            return range(ConstantesCampos.TELEFONO,
                ConstantesCampos.PAGINA_WEB+1)

    def cargar_bbdd_empresa(self):
        cursor = self.cnx.cursor()
        cursor.execute(self.DELETE_PREVIO_EMPRESA)
        self.cnx.commit()
        cursor.close()
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'contactos_empresa.csv')
        , encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
        for linea in lineas:
            datos = linea.split(';')
            telefono = str(datos[self.ConstantesCampos.TELEFONO].strip())
            nombre = str(datos[self.ConstantesCampos.NOMBRE].strip())
            fecha_ingreso = str(datos[self.ConstantesCampos.FECHA_INGRESO].
            strip())
            descripcion_empresa = str(datos[self.ConstantesCampos.
            DESCRIPCION_EMPRESA].strip())
            pagina_web = str(datos[self.ConstantesCampos.PAGINA_WEB].strip())
            inserts_empresa = f"INSERT INTO contactos_empresa (telefono, \
nombre, fecha_ingreso, descripcion_empresa, pagina_web) VALUES({telefono}, \
'{nombre}','{fecha_ingreso}','{descripcion_empresa}','{pagina_web}');"
            cursor.execute(inserts_empresa)
            self.cnx.commit()
        cursor.close()

    def cargar_bbdd_persona(self):
        cursor = self.cnx.cursor()
        cursor.execute(self.DELETE_PREVIO_PERSONA)
        self.cnx.commit()
        cursor.close()
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'contactos_persona.csv')
        , encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
        for linea in lineas:
            datos = linea.split(';')
            telefono = str(datos[self.ConstantesCampos.TELEFONO].strip())
            nombre = str(datos[self.ConstantesCampos.NOMBRE].strip())
            fecha_ingreso = str(datos[self.ConstantesCampos.FECHA_INGRESO].
            strip())
            cumpleanios = str(datos[self.ConstantesCampos.CUMPLEANIOS].
            strip())
            inserts_persona = f" INSERT INTO contactos_persona (telefono, \
nombre, fecha_ingreso, cumpleanios) VALUES({telefono},'{nombre}',\
'{fecha_ingreso}','{cumpleanios}');"
            cursor.execute(inserts_persona)
            self.cnx.commit()
        cursor.close()

#Ejecuccion().cargar_bbdd_empresa()
#Ejecuccion().cargar_bbdd_persona()
