from typing import List

from sqlalchemy import update
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.pessoa_juridica_repository import (
    PessoaJuridicaRepositoryInterface
)


class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    @property
    def limite_saque(self) -> float:
        return 60000.00

    def list_pessoas_juridicas(self) -> List[PessoaJuridica]:
        with self.__db_connection as database:
            try:
                pessoas_juridicas = database.session.query(PessoaJuridica).all()
                return pessoas_juridicas
            except NoResultFound:
                return []

    def buscar_pessoa_juridica(self, id_pessoa: int):
        with self.__db_connection as database:
            try:
                pessoa_juridica = (database.session
                                   .query(PessoaJuridica)
                                   .filter(PessoaJuridica.id == id_pessoa)
                                   .first())
                return pessoa_juridica
            except NoResultFound:
                return None

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

    def sacar_dinheiro(self, quantia, id_pessoa: int):
        if quantia > self.limite_saque:
            raise ValueError(f"Saque excede o limite de R$ {self.limite_saque}")

        pessoa_juridica = self.buscar_pessoa_juridica(id_pessoa)

        if quantia > pessoa_juridica.saldo:
            raise ValueError("Saldo insuficiente.")

        novo_saldo = pessoa_juridica.saldo - quantia
        command = (update(PessoaJuridica)
                   .where(PessoaJuridica.id == id_pessoa)
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
            pessoa_juridica = (database.session
                             .query(PessoaJuridica)
                             .filter(PessoaJuridica.id == id_pessoa)
                             .with_entities(
                                 PessoaJuridica.nome_fantasia,
                                 PessoaJuridica.saldo,
                                 PessoaJuridica.categoria
                             )
                             .first())

            return pessoa_juridica
