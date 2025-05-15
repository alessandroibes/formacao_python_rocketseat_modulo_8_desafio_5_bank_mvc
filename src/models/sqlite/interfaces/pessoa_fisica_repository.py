from abc import abstractmethod
from typing import List

from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface


class PessoaFisicaRepositoryInterface(ClienteRepositoryInterface):

    @abstractmethod
    def list_pessoas_fisicas(self) -> List[PessoaFisica]:
        pass

    @abstractmethod
    def buscar_pessoa_fisica(self, id_pessoa: int):
        pass

    @abstractmethod
    def criar_pessoa_fisica(
            self,
            renda_mensal: float,
            idade: int,
            nome_completo: str,
            celular: str,
            email: str,
            categoria: str,
            saldo: float,
        ) -> None:
        pass
