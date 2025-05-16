from typing import List

from src.models.sqlite.interfaces.pessoa_juridica_repository import (
    PessoaJuridicaRepositoryInterface
)
from .interfaces.listar_pessoas_juridicas_controller import (
    ListarPessoasJuridicasControllerInterface
)


class ListarPessoasJuridicasController(ListarPessoasJuridicasControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface):
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def listar_pessoas_juridicas(self) -> List[dict]:
        pessoas_juridicas = self.__pessoa_juridica_repository.list_pessoas_juridicas()

        return pessoas_juridicas
