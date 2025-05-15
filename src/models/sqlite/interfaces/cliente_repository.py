from abc import ABC, abstractmethod


class ClienteRepositoryInterface(ABC):

    @property
    @abstractmethod
    def limite_saque(self) -> float:
        """Limite de saque específico do tipo de cliente."""

    @abstractmethod
    def sacar_dinheiro(self, quantia, id_pessoa: int):
        pass

    @abstractmethod
    def realizar_extrato(self, id_pessoa: int):
        pass
