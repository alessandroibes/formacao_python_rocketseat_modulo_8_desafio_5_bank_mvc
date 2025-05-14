import pytest

from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository


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
