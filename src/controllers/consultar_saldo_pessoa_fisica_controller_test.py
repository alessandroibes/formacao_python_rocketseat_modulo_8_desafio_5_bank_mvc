# pylint: disable=unused-argument
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .consultar_saldo_pessoa_fisica_controller import ConsultarSaldoPessoaFisicaController

class MockPessoaFisicaRepository():
    def buscar_pessoa_fisica(self, id_pessoa: int):
        return PessoaFisica(
            id=id_pessoa,
            renda_mensal=10000.00,
            idade=22,
            nome_completo="Pessoa Física Teste",
            celular="1234-5678",
            email="pfisica@example.com",
            categoria="Categoria Teste",
            saldo=25000.00
        )


class MockPessoaFisicaRepositoryNone():
    def buscar_pessoa_fisica(self, id_pessoa: int):
        return None


def test_consultar_saldo():
    controller = ConsultarSaldoPessoaFisicaController(MockPessoaFisicaRepository())
    saldo = controller.consultar_saldo(1)

    assert saldo == 25000.00


def test_consultar_saldo_vazio():
    controller = ConsultarSaldoPessoaFisicaController(MockPessoaFisicaRepositoryNone())
    saldo = controller.consultar_saldo(1)

    assert saldo == 0
