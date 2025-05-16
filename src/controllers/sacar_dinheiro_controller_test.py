# pylint: disable=unused-argument
from .sacar_dinheiro_controller import SacarDinheiroController


pessoa_fisica = {
        "saldo": 25000.00,
    }

pessoa_juridica = {
        "saldo": 250000.00,
    }


class MockPessoaFisicaRepository():
    def criar_pessoa_fisica(self, *args, **kwargs) -> None:
        return None

    def sacar_dinheiro(self, quantia, id_pessoa: int):
        novo_saldo = pessoa_fisica["saldo"] - quantia
        return f"Saque de R$ {quantia} realizado com sucesso. Saldo restante: R$ {novo_saldo}"


class MockPessoaJuridicaRepository():
    def criar_pessoa_juridica(self, *args, **kwargs) -> None:
        return None

    def sacar_dinheiro(self, quantia, id_pessoa: int):
        novo_saldo = pessoa_juridica["saldo"] - quantia
        return f"Saque de R$ {quantia} realizado com sucesso. Saldo restante: R$ {novo_saldo}"


def test_sacar_dinheiro_pessoa_fisica():
    controller = SacarDinheiroController(MockPessoaFisicaRepository())
    resultado = controller.sacar_dinheiro(1000.0, 1)

    assert resultado == "Saque de R$ 1000.0 realizado com sucesso. Saldo restante: R$ 24000.0"


def test_sacar_dinheiro_pessoa_juridica():
    controller = SacarDinheiroController(MockPessoaJuridicaRepository())
    resultado = controller.sacar_dinheiro(1000.0, 1)

    assert resultado == "Saque de R$ 1000.0 realizado com sucesso. Saldo restante: R$ 249000.0"
