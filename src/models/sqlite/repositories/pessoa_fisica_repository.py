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

    def criar_pessoa_fisica(
            self,
            renda_mensal: float,
            idade: int,
            nome_completo: str,
            celular: str,
            email: str,
            categoria: str,
            saldo: float,
        ) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica = PessoaFisica(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_fisica)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def sacar_dinheiro(self, quantia):
        raise NotImplementedError

    def realizar_extrato(self, pessoa):
        raise NotImplementedError
