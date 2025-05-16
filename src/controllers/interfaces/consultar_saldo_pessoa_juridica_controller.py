from abc import ABC, abstractmethod


class ConsultarSaldoPessoaJuridicaControllerInterface(ABC):

    @abstractmethod
    def consultar_saldo(self, id_pessoa: int):
        pass
