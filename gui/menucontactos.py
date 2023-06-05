from datetime import datetime

from clases.contactoempresa import ContactoEmpresa
from clases.contactopersona import ContactoPersona

from gui.ctes import ANCHO_MENU, SALTOS_DE_LINEA, PERSONAL, EMPRESA
from gui.menu import Menu

class MenuAddContactos(Menu):
    class OpcionesMenuContactos:
        ANIADIR_CONTACTO_PERSONAL = 1
        ANIADIR_CONTACTO_EMPRESA = 2
        SALIR = 3

        @staticmethod
        def opciones():
            return range(MenuAddContactos.OpcionesMenuContactos.
ANIADIR_CONTACTO_PERSONAL,MenuAddContactos.OpcionesMenuContactos.SALIR+1)

    def __init__(self, app):
        self._app = app

    def main(self):
        fin = False
        while not fin:
            self._visualizar_menu()
            opcion = self._recolectar_opcion_menu()
            fin = self._tratar_opcion_menu(opcion)

    def _visualizar_menu(self):
        print("\n"*SALTOS_DE_LINEA)
        print(f"="*ANCHO_MENU)
        print(f"AÑADIR CONTACTO".center(ANCHO_MENU))
        print(f"="*ANCHO_MENU)
        print(f"1. CONTACTO PERSONAL")
        print(f"2. CONTACTO EMPRESA")
        print(f"3. VOLVER?")
        print(f"="*ANCHO_MENU)

    def _recolectar_opcion_menu(self) -> int:
        excepcion_contacto = True
        while excepcion_contacto:
            try:
                opcion = 0
                while opcion not in self.OpcionesMenuContactos.opciones():
                    opcion = int(input("¿QUÉ TIPO DE CONTACTO \
DESEAS AÑADIR?: "))
            except ValueError:
                print(f"DEBE INGRESAR UN NÚMERO")
            else:
                return opcion

    def _tratar_opcion_menu(self, opcion) -> bool:
        if opcion == self.OpcionesMenuContactos.ANIADIR_CONTACTO_PERSONAL:
            self._tratar_opcion_add_nuevo_contacto_personal()
        elif opcion == self.OpcionesMenuContactos.ANIADIR_CONTACTO_EMPRESA:
            self._tratar_opcion_add_nuevo_contacto_empresa()
        elif opcion == self.OpcionesMenuContactos.SALIR:
            return True
        else:
            print(f"OPCION ERRÓNEA")
        return False

    def _tratar_opcion_add_nuevo_contacto_personal(self):
        telefono = self._solicitar_telefono()
        (tipo, fecha_ingreso, cumpleanios, 
        nombre_personal) = self._pedir_datos_nuevo_contacto_personal()
        self._add_nuevo_contacto_personal(tipo, telefono, 
        fecha_ingreso, cumpleanios, nombre_personal)
    
    def _tratar_opcion_add_nuevo_contacto_empresa(self):
        telefono = self._solicitar_telefono()
        (tipo, fecha_ingreso, nombre_empresa, descripcion_empresa, 
        pagina_web)  = self._pedir_datos_nuevo_contacto_empresa() 
        self._add_nuevo_contacto_empresa(tipo, telefono, 
        fecha_ingreso, nombre_empresa, descripcion_empresa, pagina_web)
    
    def _add_nuevo_contacto_personal(self, tipo, telefono, 
    fecha_ingreso, cumpleanios, nombre_personal):
        self._app.contactos._add_contacto_personal(
        ContactoPersona(tipo, telefono, nombre_personal, fecha_ingreso, cumpleanios))
    
    def _add_nuevo_contacto_empresa(self, tipo, telefono,
     nombre_empresa, fecha_ingreso,  descripcion_empresa, pagina_web):
        self._app.contactos._add_contacto_empresa(
        ContactoEmpresa(tipo, telefono, nombre_empresa, fecha_ingreso, descripcion_empresa, pagina_web))

    def _solicitar_telefono(self):
        excepcion = True
        while excepcion:
            try:
                telefono = None
                while not telefono:
                    telefono = int(input("TELÉFONO: "))
            except ValueError:
                print(f"DEBE INGRESAR UNA CADENA DE 9 DÍGITOS")
            else:
                if self._app.validator.expresion_telefono(telefono):
                    return telefono
                else:
                    print(f"EL Nº DE TELÉFONO DEBE TENER 9 DÍGITOS")
    
    def _pedir_datos_nuevo_contacto_personal(self):
        now = datetime.now()
        sysdate = now.strftime("%Y-%m-%d %H:%M:%S")
        fecha_ingreso = sysdate
        tipo = PERSONAL
        nombre_validado = cumpleanios_validado = True
        while nombre_validado:
            nombre_personal = input("NOMBRE COMPLETO: ")
            if not self._app.validator.expresion_nombre(nombre_personal):
                print(f"NOMBRE INCORRECTO")
            else:
                nombre_validado = False
        while cumpleanios_validado:
            cumpleanios = input("FECHA DE NACIMIENTO(YYYY-MM-DD): ")
            if not self._app.validator.expresion_cumpleanios(cumpleanios):
                print(f"FORMATO INCORRECTO")
            else:
                cumpleanios_validado = False
        return tipo, fecha_ingreso, cumpleanios, nombre_personal

    def _pedir_datos_nuevo_contacto_empresa(self):
        now = datetime.now()
        sysdate = now.strftime("%Y-%m-%d %H:%M:%S")
        fecha_ingreso = sysdate
        tipo = EMPRESA
        nombre_empresa_validado = True
        while nombre_empresa_validado:
            nombre_empresa = input("NOMBRE COMPLETO: ")
            if (not self._app.validator.
            expresion_nombre_empresa(nombre_empresa)):
                print(f"NOMBRE INCORRECTO")
            else:
                nombre_empresa_validado = False
                descripcion_empresa = input("DESCRIPCIÓN \
DE LA EMPRESA: ")
                pagina_web = input("PAGINA WEB: ")
        return (tipo, nombre_empresa, fecha_ingreso, 
        descripcion_empresa, pagina_web)