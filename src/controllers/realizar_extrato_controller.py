from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface
from .interfaces.realizar_extrato_controller import RealizarExtratoControllerInterface


class RealizarExtratoController(RealizarExtratoControllerInterface):
    def __init__(self, client_repository: ClienteRepositoryInterface):
        self.__client_repository = client_repository

    def realizar_extrato(self, id_pessoa: int):
        extrato = self.__client_repository.realizar_extrato(id_pessoa)
        return extrato
