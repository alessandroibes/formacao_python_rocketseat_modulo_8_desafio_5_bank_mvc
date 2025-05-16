from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface
from .interfaces.sacar_dinheiro_controller import SacarDinheiroControllerInterface


class SacarDinheiroController(SacarDinheiroControllerInterface):
    def __init__(self, client_repository: ClienteRepositoryInterface):
        self.__client_repository = client_repository

    def sacar_dinheiro(self, quantia, id_pessoa: int):
        resultado = self.__client_repository.sacar_dinheiro(quantia, id_pessoa)
        return resultado
