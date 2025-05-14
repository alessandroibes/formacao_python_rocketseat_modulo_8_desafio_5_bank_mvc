from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .pessoa_fisica_repository import PessoaFisicaRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PessoaFisica)], # query
                    [
                        PessoaFisica(
                            id=1,
                            renda_mensal=5000.00,
                            idade=35,
                            nome_completo="João da Silva",
                            celular="9999-8888",
                            email="joao@example.com",
                            categoria="Categoria A",
                            saldo=10000.00
                        ),
                        PessoaFisica(
                            id=2,
                            renda_mensal=4000.00,
                            idade=45,
                            nome_completo="Maria Oliveira",
                            celular="7777-6666",
                            email="maria@example.com",
                            categoria="Categoria B",
                            saldo=15000.00
                        )
                    ]
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_pessoas_fisicas():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_pessoas_fisicas()

    assert response[0].idade == 35
    assert response[1].idade == 45
    assert response[0].renda_mensal == 5000.00
    assert response[1].renda_mensal == 4000.00
    assert response[0].nome_completo == "João da Silva"
    assert response[1].nome_completo == "Maria Oliveira"
    assert response[0].celular == "9999-8888"
    assert response[1].celular == "7777-6666"
    assert response[0].email == "joao@example.com"
    assert response[1].email == "maria@example.com"
    assert response[0].categoria == "Categoria A"
    assert response[1].categoria == "Categoria B"
    assert response[0].saldo == 10000.00
    assert response[1].saldo == 15000.00
