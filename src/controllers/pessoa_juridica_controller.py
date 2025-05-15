import re

from src.models.sqlite.interfaces.pessoa_juridica_repository import (
    PessoaJuridicaRepositoryInterface
)


class PessoaJuridicaController:
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface):
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def criar(self, pessoa_juridica: dict) -> dict:
        faturamento = pessoa_juridica["faturamento"]
        idade = pessoa_juridica["idade"]
        nome_fantasia = pessoa_juridica["nome_fantasia"]
        celular = pessoa_juridica["celular"]
        email_corporativo = pessoa_juridica["email_corporativo"]
        categoria = pessoa_juridica["categoria"]
        saldo = pessoa_juridica["saldo"]

        self.__validate_pessoa_juridica(
            nome_fantasia,
            faturamento,
            saldo)
        self.__insert_pessoa_juridica_in_db(
            faturamento,
            idade,
            nome_fantasia,
            celular,
            email_corporativo,
            categoria,
            saldo
        )
        formated_response = self.__format_response(pessoa_juridica)
        return formated_response

    def __validate_pessoa_juridica(self,
            nome_fantasia: str,
            faturamento: float,
            saldo: float
    ) -> None:
        self.__validate_nome_fantasia(nome_fantasia)
        self.__validate_faturamento(faturamento)
        self.__validate_saldo(saldo)

    def __validate_nome_fantasia(self, nome_fantasia: str) -> None:
        pattern = r"^([A-ZÁÉÍÓÚ][a-záéíóú]+(?: [A-ZÁÉÍÓÚ][a-záéíóú]+)+)$"

        if not re.match(pattern, nome_fantasia):
            raise Exception("Nome da empresa inválido.")

    def __validate_faturamento(self, faturamento: float) -> None:
        if faturamento < 0:
            raise Exception("O faturamento não pode ser negativo.")

    def __validate_saldo(self, saldo: float) -> None:
        if saldo < 0:
            raise Exception("O saldo não pode ser negativo.")

    def __insert_pessoa_juridica_in_db(self,
        faturamento: float,
        idade: int,
        nome_fantasia: str,
        celular: str,
        email_corporativo: str,
        categoria: str,
        saldo: float
    ) -> None:
        self.__pessoa_juridica_repository.criar_pessoa_juridica(
            faturamento,
            idade,
            nome_fantasia,
            celular,
            email_corporativo,
            categoria,
            saldo
        )

    def __format_response(self, pessoa_juridica: dict) -> dict:
        return {
            "data": {
                "type": "Pessoa Jurídica",
                "count": 1,
                "attributes": pessoa_juridica
            }
        }
