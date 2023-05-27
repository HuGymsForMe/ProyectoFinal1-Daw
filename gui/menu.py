from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def _tratar_opcion_menu(self, opcion) -> bool:
        # return: True cuando haya que terminar el menú
        pass

    @abstractmethod
    def _visualizar_menu(self):
        pass

    @abstractmethod
    def _recolectar_opcion_menu(self) -> int:
        pass