# pylint: disable=unused-argument
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from .consultar_saldo_pessoa_juridica_controller import (
    ConsultarSaldoPessoaJuridicaController
)

class MockPessoaJuridicaRepository():
    def buscar_pessoa_juridica(self, id_pessoa: int):
        return PessoaJuridica(
            id=id_pessoa,
            faturamento=100000.00,
            idade=5,
            nome_fantasia="Empresa Teste",
            celular="8765-4321",
            email_corporativo="empresa_teste@example.com",
            categoria="Categoria Teste",
            saldo=250000.00
        )


class MockPessoaJuridicaRepositoryNone():
    def buscar_pessoa_juridica(self, id_pessoa: int):
        return None


def test_consultar_saldo():
    controller = ConsultarSaldoPessoaJuridicaController(MockPessoaJuridicaRepository())
    saldo = controller.consultar_saldo(1)

    assert saldo == 250000.00


def test_consultar_saldo_vazio():
    controller = ConsultarSaldoPessoaJuridicaController(MockPessoaJuridicaRepositoryNone())
    saldo = controller.consultar_saldo(1)

    assert saldo == 0
