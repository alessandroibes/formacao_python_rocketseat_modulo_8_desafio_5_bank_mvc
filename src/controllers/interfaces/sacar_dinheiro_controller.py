from abc import ABC, abstractmethod


class SacarDinheiroControllerInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, quantia, id_pessoa: int):
        pass
