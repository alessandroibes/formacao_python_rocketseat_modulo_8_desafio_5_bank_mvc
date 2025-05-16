from abc import ABC, abstractmethod


class ConsultarSaldoPessoaFisicaControllerInterface(ABC):

    @abstractmethod
    def consultar_saldo(self, id_pessoa: int):
        pass
