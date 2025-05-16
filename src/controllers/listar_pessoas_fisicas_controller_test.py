from typing import List

from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .listar_pessoas_fisicas_controller import ListarPessoasFisicasController


pessoa_fisica_1 = PessoaFisica(
    id=1,
    renda_mensal=10000.00,
    idade=22,
    nome_completo="Pessoa Física Teste",
    celular="1234-5678",
    email="pfisica@example.com",
    categoria="Categoria Teste",
    saldo=25000.00
)


pessoa_fisica_2 = PessoaFisica(
    id=2,
    renda_mensal=15000.00,
    idade=35,
    nome_completo="Pessoa Física Teste 2",
    celular="9999-8888",
    email="pfisica2@example.com",
    categoria="Categoria Teste 2",
    saldo=32000.00
)


class MockPessoaFisicaRepository():
    def list_pessoas_fisicas(self) -> List[PessoaFisica]:
        return [pessoa_fisica_1, pessoa_fisica_2]


def test_listar_pessoas_fisicas():
    controller = ListarPessoasFisicasController(MockPessoaFisicaRepository())
    pessoas_fisicas = controller.listar_pessoas_fisicas()

    expected_result = [pessoa_fisica_1, pessoa_fisica_2]

    assert expected_result == pessoas_fisicas
