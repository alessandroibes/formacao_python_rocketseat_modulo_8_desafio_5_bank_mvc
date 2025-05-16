from typing import List

from src.models.sqlite.interfaces.pessoa_fisica_repository import (
    PessoaFisicaRepositoryInterface
)
from .interfaces.listar_pessoas_fisicas_controller import (
    ListarPessoasFisicasControllerInterface
)


class ListarPessoasFisicasController(ListarPessoasFisicasControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def listar_pessoas_fisicas(self) -> List[dict]:
        pessoas_fisicas = self.__pessoa_fisica_repository.list_pessoas_fisicas()

        if pessoas_fisicas:
            return [pessoa_fisica.to_dict() for pessoa_fisica in pessoas_fisicas]

        return pessoas_fisicas
