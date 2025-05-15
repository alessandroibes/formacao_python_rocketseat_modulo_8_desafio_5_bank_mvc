from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from .pessoa_juridica_repository import PessoaJuridicaRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PessoaJuridica)], # query
                    [
                        PessoaJuridica(
                            id=1,
                            faturamento=100000.00,
                            idade=10,
                            nome_fantasia="Empresa XYZ",
                            celular="1111-2222",
                            email_corporativo="contato@empresa.com",
                            categoria="Categoria A",
                            saldo=50000.00
                        ),
                        PessoaJuridica(
                            id=2,
                            faturamento=80000.00,
                            idade=5,
                            nome_fantasia="Empresa ABC",
                            celular="3333-4444",
                            email_corporativo="contato@abc.com",
                            categoria="Categoria B",
                            saldo=70000.00
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


def test_list_pessoas_juridicas():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    response = repo.list_pessoas_juridicas()

    assert response[0].faturamento == 100000.00
    assert response[1].faturamento == 80000.00
    assert response[0].idade == 10
    assert response[1].idade == 5
    assert response[0].nome_fantasia == "Empresa XYZ"
    assert response[1].nome_fantasia == "Empresa ABC"
    assert response[0].celular == "1111-2222"
    assert response[1].celular == "3333-4444"
    assert response[0].email_corporativo == "contato@empresa.com"
    assert response[1].email_corporativo == "contato@abc.com"
    assert response[0].categoria == "Categoria A"
    assert response[1].categoria == "Categoria B"
    assert response[0].saldo == 50000.00
    assert response[1].saldo == 70000.00


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

    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    repo.criar_pessoa_juridica(**pessoa_juridica)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    mock_connection.session.rollback.assert_not_called()


def test_criar_pessoa_juridica_error():
    pessoa_juridica = {
        "faturamento": mock.ANY,
        "idade": mock.ANY,
        "nome_fantasia": mock.ANY,
        "celular": mock.ANY,
        "email_corporativo": mock.ANY,
        "categoria": mock.ANY,
        "saldo": mock.ANY
    }

    mock_connection = MockConnectionWithError()
    repo = PessoaJuridicaRepository(mock_connection)

    with pytest.raises(Exception):
        repo.criar_pessoa_juridica(**pessoa_juridica)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.rollback.assert_called_once()
    mock_connection.session.commit.assert_not_called()


def test_realizar_extrato():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    repo.realizar_extrato(1)

    mock_connection.session.filter.assert_called_once_with(PessoaJuridica.id == 1)
    mock_connection.session.with_entities.assert_called_once_with(
        PessoaJuridica.nome_fantasia,
        PessoaJuridica.saldo,
        PessoaJuridica.categoria
    )
