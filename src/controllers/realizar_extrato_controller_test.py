# pylint: disable=unused-argument
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from .realizar_extrato_controller import RealizarExtratoController


pessoa_fisica = {
        "renda_mensal": 10000.00,
        "idade": 22,
        "nome_completo": "Pessoa Física Teste",
        "celular": "1234-5678",
        "email": "pfisica@example.com",
        "categoria": "Categoria Teste",
        "saldo": 25000.00,
    }


pessoa_juridica = {
        "faturamento": 100000.00,
        "idade": 5,
        "nome_fantasia": "Empresa Teste",
        "celular": "8765-4321",
        "email_corporativo": "empresa_teste@example.com",
        "categoria": "Categoria Teste",
        "saldo": 250000.00,
    }


class MockPessoaFisicaRepository():
    def realizar_extrato(self, id_pessoa: int):
        return PessoaFisica(
            nome_completo=pessoa_fisica["nome_completo"],
            idade=pessoa_fisica["idade"],
            saldo=pessoa_fisica["saldo"],
            categoria=pessoa_fisica["categoria"]
        )


class MockPessoaJuridicaRepository():
    def realizar_extrato(self, id_pessoa: int):
        return PessoaJuridica(
            nome_fantasia=pessoa_juridica["nome_fantasia"],
            idade=pessoa_juridica["idade"],
            saldo=pessoa_juridica["saldo"],
            categoria=pessoa_juridica["categoria"]
        )


def test_realizar_extrato_pessoa_fisica():
    controller = RealizarExtratoController(MockPessoaFisicaRepository())
    extrato = controller.realizar_extrato(1)

    assert str(extrato) == "Nome: Pessoa Física Teste, Idade: 22, Saldo: 25000.0"


def test_realizar_extrato_pessoa_juridica():
    controller = RealizarExtratoController(MockPessoaJuridicaRepository())
    extrato = controller.realizar_extrato(1)

    assert str(extrato) == "Nome Fantasia: Empresa Teste, Idade: 5, Saldo: 250000.0"
