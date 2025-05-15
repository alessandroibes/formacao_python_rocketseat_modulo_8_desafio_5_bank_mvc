from typing import List

from sqlalchemy import update
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface


class PessoaFisicaRepository(ClienteRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    @property
    def limite_saque(self) -> float:
        return 12000.00

    def list_pessoas_fisicas(self) -> List[PessoaFisica]:
        with self.__db_connection as database:
            try:
                pessoas_fisicas = database.session.query(PessoaFisica).all()
                return pessoas_fisicas
            except NoResultFound:
                return []

    def buscar_pessoa_fisica(self, id_pessoa: int):
        with self.__db_connection as database:
            try:
                pessoa_fisica = (database.session
                                   .query(PessoaFisica)
                                   .filter(PessoaFisica.id == id_pessoa)
                                   .first())
                return pessoa_fisica
            except NoResultFound:
                return None

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

    def sacar_dinheiro(self, quantia, id_pessoa: int):
        if quantia > self.limite_saque:
            raise ValueError(f"Saque excede o limite de R$ {self.limite_saque}")

        pessoa_fisica = self.buscar_pessoa_fisica(id_pessoa)

        if quantia > pessoa_fisica.saldo:
            raise ValueError("Saldo insuficiente.")

        novo_saldo = pessoa_fisica.saldo - quantia
        command = (update(PessoaFisica)
                   .where(PessoaFisica.id == id_pessoa)
                   .values(saldo=novo_saldo))
        with self.__db_connection as database:
            try:
                database.session.execute(command)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

        return f"Saque de R$ {quantia} realizado com sucesso. Saldo restante: R$ {novo_saldo}"

    def realizar_extrato(self, id_pessoa: int):
        with self.__db_connection as database:
            pessoa_fisica = (database.session
                             .query(PessoaFisica)
                             .filter(PessoaFisica.id == id_pessoa)
                             .with_entities(
                                 PessoaFisica.nome_completo,
                                 PessoaFisica.saldo,
                                 PessoaFisica.categoria
                             )
                             .first())

            return pessoa_fisica
