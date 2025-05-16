from typing import List

from src.models.sqlite.interfaces.pessoa_fisica_repository import (
    PessoaFisicaRepositoryInterface
)


class ListarPessoasFisicasController():
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def listar_pessoas_fisicas(self) -> List[dict]:
        pessoas_fisicas = self.__pessoa_fisica_repository.list_pessoas_fisicas()

        return pessoas_fisicas
