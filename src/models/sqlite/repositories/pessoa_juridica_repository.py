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

    def criar_pessoa_juridica(
            self,
            faturamento: float,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: float,
        ) -> None:
        with self.__db_connection as database:
            try:
                pessoa_juridica = PessoaJuridica(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_juridica)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def sacar_dinheiro(self, quantia):
        raise NotImplementedError

    def realizar_extrato(self, id_pessoa: int):
        raise NotImplementedError
