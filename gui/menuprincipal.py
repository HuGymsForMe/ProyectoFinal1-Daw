import abc

from clases.agenda import Agenda

from gui.ctes import ANCHO_MENU, SALTOS_DE_LINEA
from gui.menu import Menu
from gui.menucontactos import MenuAddContactos

class MenuAgenda(Menu):
    class OpcionesMenuAgenda:
        ANIADIR_CONTACTO = 1
        ELIMINAR_CONTACTO = 2
        LISTAR_CONTACTOS = 3
        BUSCAR_CONTACTO = 4
        EXISTE_CONTACTO = 5
        SALIR = 6

        @staticmethod
        def opciones():
            return range(MenuAgenda.OpcionesMenuAgenda.ANIADIR_CONTACTO,
                        MenuAgenda.OpcionesMenuAgenda.SALIR+1)
    
    def __init__(self, app):
        self._app = app
        self.menu_aniadir_contactos = MenuAddContactos(self._app)
    
    def main(self):
        fin = False
        while not fin:
            self._visualizar_menu()
            opcion_menu = self._recolectar_opcion_menu()
            fin = self._tratar_opcion_menu(opcion_menu)

    def _visualizar_menu(self):
        print(f"\n"*SALTOS_DE_LINEA)
        print(f"="*ANCHO_MENU)
        print(f"MI AGENDA".center(ANCHO_MENU))
        print(f"="*ANCHO_MENU)
        print(f"OPCIONES".center(ANCHO_MENU))
        print("="*ANCHO_MENU)
        print(f"1. AÑADIR UN CONTACTO") 
        print(f"2. ELIMINAR UN CONTACTO") 
        print(f"3. LISTAR MIS CONTACTOS") 
        print(f"4. BUSCAR UN CONTACTO")
        print(f"5. EXISTE UN CONTACTO?")
        print(f"6. SALIR?")
        print(f"="*ANCHO_MENU)

    def _recolectar_opcion_menu(self) -> int:
        excepcion_menu = True
        while excepcion_menu:
            try:
                opcion = 0
                while opcion not in self.OpcionesMenuAgenda.opciones():
                    opcion = int(input("¿QUÉ DESEAS HACER?: "))
            except ValueError:
                print(f"DEBE INGRESAR UN NÚMERO")
            else:
                return opcion
                
    def _tratar_opcion_menu(self, opcion) -> bool:
        if opcion == self.OpcionesMenuAgenda.ANIADIR_CONTACTO:
           self.menu_aniadir_contactos.main()
        elif opcion == self.OpcionesMenuAgenda.ELIMINAR_CONTACTO:
            self._tratar_opcion_borrar_contacto()
        elif opcion == self.OpcionesMenuAgenda.LISTAR_CONTACTOS:
            self._tratar_opcion_listar_contactos()
        elif opcion == self.OpcionesMenuAgenda.BUSCAR_CONTACTO:
            self._tratar_opcion_buscar_contacto()
        elif opcion == self.OpcionesMenuAgenda.EXISTE_CONTACTO:
            self._tratar_opcion_existe_contacto()            
        elif opcion == self.OpcionesMenuAgenda.SALIR:
            self._good_bye()
            return True
        return False

    def _tratar_opcion_borrar_contacto(self):
        contacto_buscado = self._pedir_nombre_borrar_contacto()
        self._mensaje_borrado_contacto(contacto_buscado)

    def _tratar_opcion_listar_contactos(self):
        print("="*ANCHO_MENU)
        print("MIS CONTACTOS".center(ANCHO_MENU))
        print("="*ANCHO_MENU)
        for contacto in self._app.contactos._contactos:
            print(f"{repr(contacto)}")
            print("="*ANCHO_MENU)
        
    def _tratar_opcion_buscar_contacto(self):
        nombre = self._pedir_nombre_buscar_existe_contacto()
        self._mensaje_buscado_contacto(nombre)

    def _tratar_opcion_existe_contacto(self):
        nombre = self._pedir_nombre_buscar_existe_contacto()
        self._mensaje_existe_contacto(nombre)
    
    def _mensaje_borrado_contacto(self, contacto_buscado:str):
        if self._app.contactos.del_contacto(contacto_buscado):
            print(f"CONTACTO ELIMINADO")
        else:
            print(f"NO EXISTE EL CONTACTO")

    def _mensaje_buscado_contacto(self, nombre:str):
        if self._app.contactos.busqueda_contacto(nombre):
            print(f"="*ANCHO_MENU)
            print(f"CONTACTO ENCONTRADO".center(ANCHO_MENU))
            print(f"="*ANCHO_MENU)
            for indice in self._app.contactos._contactos:
                if self._app.contactos._contactos[indice]._nombre == nombre:
                    print(repr(self._app.contactos._contactos[indice]))
            print(f"="*ANCHO_MENU)
        else:
            print(f"CONTACTO NO ENCONTRADO")

    def _mensaje_existe_contacto(self, nombre:str):
        if self._app.contactos.busqueda_contacto(nombre):
            print(f"EL CONTACTO EXISTE")
        else:
            print(f"EL CONTACTO NO EXISTE")

    @staticmethod
    def _pedir_nombre_borrar_contacto():
        contacto_buscado = input("CONTACTO A BORRAR: ")
        return contacto_buscado
    
    @staticmethod
    def _pedir_nombre_buscar_existe_contacto():
        nombre = input("ESCRIBEME EL NOMBRE DE UN CONTACTO: ")
        return nombre

    @staticmethod
    def _good_bye():
        print("\nHASTA LA PRÓXIMA")

