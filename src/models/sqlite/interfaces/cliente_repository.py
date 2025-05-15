from abc import ABC, abstractmethod


class ClienteRepositoryInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, quantia):
        pass

    @abstractmethod
    def realizar_extrato(self, id_pessoa: int):
        pass
