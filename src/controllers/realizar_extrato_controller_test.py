# pylint: disable=unused-argument
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
        return "Nome Completo: Pessoa Física Teste, Categoria: Categoria Teste, Saldo: 25000.0"


class MockPessoaJuridicaRepository():
    def realizar_extrato(self, id_pessoa: int):
        return "Nome Fantasia: Empresa Teste, Categoria: Categoria Teste, Saldo: 250000.0"


def test_realizar_extrato_pessoa_fisica():
    controller = RealizarExtratoController(MockPessoaFisicaRepository())
    extrato = controller.realizar_extrato(1)

    expected = "Nome Completo: Pessoa Física Teste, Categoria: Categoria Teste, Saldo: 25000.0"

    assert str(extrato) == expected


def test_realizar_extrato_pessoa_juridica():
    controller = RealizarExtratoController(MockPessoaJuridicaRepository())
    extrato = controller.realizar_extrato(1)

    expected = "Nome Fantasia: Empresa Teste, Categoria: Categoria Teste, Saldo: 250000.0"

    assert str(extrato) == expected
