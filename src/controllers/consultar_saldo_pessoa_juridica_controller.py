from src.models.sqlite.interfaces.pessoa_juridica_repository import (
    PessoaJuridicaRepositoryInterface
)
from .interfaces.consultar_saldo_pessoa_juridica_controller import (
    ConsultarSaldoPessoaJuridicaControllerInterface
)

class ConsultarSaldoPessoaJuridicaController(ConsultarSaldoPessoaJuridicaControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface):
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def consultar_saldo(self, id_pessoa: int):
        pessoa_juridica = self.__pessoa_juridica_repository.buscar_pessoa_juridica(id_pessoa)

        if pessoa_juridica:
            return pessoa_juridica.saldo

        return 0
