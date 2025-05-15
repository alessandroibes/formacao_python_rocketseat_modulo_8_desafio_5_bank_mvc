import pytest

from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository
from .pessoa_juridica_repository import PessoaJuridicaRepository


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="database integration")
def test_list_pessoas_fisicas():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.list_pessoas_fisicas()
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_criar_pessoa_fisica():
    pessoa_fisica = {
        "renda_mensal": 12000.00,
        "idade": 42,
        "nome_completo": "José Firmino",
        "celular": "1234-4321",
        "email": "josefi@exemplo.com",
        "categoria": "Categoria D",
        "saldo": 45000.00
    }

    repo = PessoaFisicaRepository(db_connection_handler)
    repo.criar_pessoa_fisica(**pessoa_fisica)


@pytest.mark.skip(reason="database integration")
def test_realizar_extrato():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.realizar_extrato(1)
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_list_pessoas_juridicas():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.list_pessoas_juridicas()
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_criar_pessoa_juridica():
    pessoa_juridica = {
        "faturamento": 85000.00,
        "idade": 7,
        "nome_fantasia": "Empresa CBA",
        "celular": "1234-9999",
        "email_corporativo": "cba@exemplo.com",
        "categoria": "Categoria E",
        "saldo": 125000.00
    }

    repo = PessoaJuridicaRepository(db_connection_handler)
    repo.criar_pessoa_juridica(**pessoa_juridica)
