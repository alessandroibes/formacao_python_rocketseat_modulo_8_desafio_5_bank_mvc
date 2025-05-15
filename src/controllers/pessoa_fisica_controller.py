import re

from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface


class PessoaFisicaController:
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def criar(self, pessoa_fisica: dict) -> dict:
        renda_mensal = pessoa_fisica["renda_mensal"]
        idade = pessoa_fisica["idade"]
        nome_completo = pessoa_fisica["nome_completo"]
        celular = pessoa_fisica["celular"]
        email = pessoa_fisica["email"]
        categoria = pessoa_fisica["categoria"]
        saldo = pessoa_fisica["saldo"]

        self.__validate_pessoa_fisica(
            nome_completo,
            renda_mensal,
            saldo)
        self.__insert_pessoa_fisica_in_db(
            renda_mensal,
            idade,
            nome_completo,
            celular,
            email,
            categoria,
            saldo
        )
        formated_response = self.__format_response(pessoa_fisica)
        return formated_response

    def __validate_pessoa_fisica(self,
            nome_completo: str,
            renda_mensal: float,
            saldo: float
    ) -> None:
        self.__validate_nome_completo(nome_completo)
        self.__validate_renda_mensal(renda_mensal)
        self.__validate_saldo(saldo)

    def __validate_nome_completo(self, nome_completo: str) -> None:
        pattern = r"^([A-ZÁÉÍÓÚ][a-záéíóú]+(?: [A-ZÁÉÍÓÚ][a-záéíóú]+)+)$"

        if not re.match(pattern, nome_completo):
            raise Exception("Nome da pessoa inválido.")

    def __validate_renda_mensal(self, renda_mensal: float) -> None:
        if renda_mensal < 0:
            raise Exception("A renda mensal não pode ser negativa.")

    def __validate_saldo(self, saldo: float) -> None:
        if saldo < 0:
            raise Exception("O saldo não pode ser negativo.")

    def __insert_pessoa_fisica_in_db(self,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float
    ) -> None:
        self.__pessoa_fisica_repository.criar_pessoa_fisica(
            renda_mensal,
            idade,
            nome_completo,
            celular,
            email,
            categoria,
            saldo
        )

    def __format_response(self, pessoa_fisica: dict) -> dict:
        return {
            "data": {
                "type": "Pessoa Física",
                "count": 1,
                "attributes": pessoa_fisica
            }
        }
