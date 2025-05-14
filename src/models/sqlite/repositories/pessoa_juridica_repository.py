from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface


class PessoaJuridicaRepository(ClienteRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoas_juridicas(self) -> List[PessoaJuridica]:
        with self.__db_connection as database:
            try:
                pessoas_juridicas = database.session.query(PessoaJuridica).all()
                return pessoas_juridicas
            except NoResultFound:
                return []

    def sacar_dinheiro(self, quantia):
        raise NotImplementedError

    def realizar_extrato(self, pessoa):
        raise NotImplementedError
