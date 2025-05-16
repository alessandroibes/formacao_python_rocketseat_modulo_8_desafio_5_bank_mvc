from src.models.sqlite.interfaces.pessoa_fisica_repository import (
    PessoaFisicaRepositoryInterface
)
from .interfaces.consultar_saldo_pessoa_fisica_controller import (
    ConsultarSaldoPessoaFisicaControllerInterface
)


class ConsultarSaldoPessoaFisicaController(ConsultarSaldoPessoaFisicaControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def consultar_saldo(self, id_pessoa: int):
        pessoa_fisica = self.__pessoa_fisica_repository.buscar_pessoa_fisica(id_pessoa)

        if pessoa_fisica:
            return pessoa_fisica.saldo

        return 0
