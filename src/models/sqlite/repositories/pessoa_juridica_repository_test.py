from unittest import mock
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
