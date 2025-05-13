from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface


class PessoaFisicaRepository(ClienteRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoas_fisicas(self) -> List[PessoaFisica]:
        with self.__db_connection as database:
            try:
                pessoas_fisicas = database.session.query(PessoaFisica).all()
                return pessoas_fisicas
            except NoResultFound:
                return []

    def sacar_dinheiro(self, quantia):
        raise NotImplementedError

    def realizar_extrato(self, pessoa):
        raise NotImplementedError
