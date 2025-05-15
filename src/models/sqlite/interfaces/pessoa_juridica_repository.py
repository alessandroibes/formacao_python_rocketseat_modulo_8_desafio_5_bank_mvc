from abc import abstractmethod
from typing import List

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface


class PessoaJuridicaRepositoryInterface(ClienteRepositoryInterface):

    @abstractmethod
    def list_pessoas_juridicas(self) -> List[PessoaJuridica]:
        pass

    @abstractmethod
    def buscar_pessoa_juridica(self, id_pessoa: int):
        pass

    @abstractmethod
    def criar_pessoa_juridica(
            self,
            faturamento: float,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: float,
        ) -> None:
        pass
