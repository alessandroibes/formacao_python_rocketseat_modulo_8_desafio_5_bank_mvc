from abc import ABC, abstractmethod


class RealizarExtratoControllerInterface(ABC):

    @abstractmethod
    def realizar_extrato(self, id_pessoa: int):
        pass
