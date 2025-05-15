from unittest import mock
import pytest
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


class MockConnectionWithError:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.add.side_effect = self.__raise_exception

    def __raise_exception(self, *args, **kwargs):
        raise Exception("Generic error")

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

    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    repo.criar_pessoa_fisica(**pessoa_fisica)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    mock_connection.session.rollback.assert_not_called()


def test_criar_pessoa_fisica_error():
    pessoa_fisica = {
        "renda_mensal": mock.ANY,
        "idade": mock.ANY,
        "nome_completo": mock.ANY,
        "celular": mock.ANY,
        "email": mock.ANY,
        "categoria": mock.ANY,
        "saldo": mock.ANY
    }

    mock_connection = MockConnectionWithError()
    repo = PessoaFisicaRepository(mock_connection)

    with pytest.raises(Exception):
        repo.criar_pessoa_fisica(**pessoa_fisica)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.rollback.assert_called_once()
    mock_connection.session.commit.assert_not_called()


def test_realizar_extrato():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    repo.realizar_extrato(1)

    mock_connection.session.filter.assert_called_once_with(PessoaFisica.id == 1)
    mock_connection.session.with_entities.assert_called_once_with(
        PessoaFisica.nome_completo,
        PessoaFisica.saldo,
        PessoaFisica.categoria
    )
