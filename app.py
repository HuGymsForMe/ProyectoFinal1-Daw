import gui.menuprincipal as menu_principal

from clases.agenda import Agenda
from clases.validator import Validator

class ProgramaAgenda:
    def __init__(self):
        self.menu_principal = menu_principal.MenuAgenda(self)
        self.contactos = Agenda()
        self.validator = Validator()
    
    def main(self):
        self.contactos.cargar_ficheros()
        self.menu_principal.main()
        self.contactos.sobreescribir_ficheros()

if __name__ == "__main__":
    ProgramaAgenda().main()