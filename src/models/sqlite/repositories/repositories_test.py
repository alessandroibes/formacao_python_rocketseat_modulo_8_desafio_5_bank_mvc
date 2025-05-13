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
