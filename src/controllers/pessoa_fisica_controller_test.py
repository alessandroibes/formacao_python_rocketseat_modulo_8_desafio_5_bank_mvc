# pylint: disable=unused-argument
import copy
import pytest

from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .pessoa_fisica_controller import PessoaFisicaController


pessoa_fisica = {
        "renda_mensal": 10000.00,
        "idade": 22,
        "nome_completo": "Pessoa Física Teste",
        "celular": "1234-5678",
        "email": "pfisica@example.com",
        "categoria": "Categoria Teste",
        "saldo": 25000.00,
    }


class MockPessoaFisicaRepository():
    def criar_pessoa_fisica(self, *args, **kwargs) -> None:
        return None

    def sacar_dinheiro(self, quantia, id_pessoa: int):
        novo_saldo = pessoa_fisica["saldo"] - quantia
        return f"Saque de R$ {quantia} realizado com sucesso. Saldo restante: R$ {novo_saldo}"

    def realizar_extrato(self, id_pessoa: int):
        return PessoaFisica(
            nome_completo=pessoa_fisica["nome_completo"],
            idade=pessoa_fisica["idade"],
            saldo=pessoa_fisica["saldo"],
            categoria=pessoa_fisica["categoria"]
        )


def test_criar():
    controller = PessoaFisicaController(MockPessoaFisicaRepository())
    response = controller.criar(pessoa_fisica)

    assert response["data"]["type"] == "Pessoa Física"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_fisica


def test_criar_com_nome_completo_invalido():
    copia_pessoa_fisica = copy.deepcopy(pessoa_fisica)
    copia_pessoa_fisica["nome_completo"] = "NomeInválido123"

    controller = PessoaFisicaController(MockPessoaFisicaRepository())

    with pytest.raises(Exception) as error:
        controller.criar(copia_pessoa_fisica)

    assert str(error.value) == "Nome da pessoa inválido."


def test_criar_com_renda_mensal_invalida():
    copia_pessoa_fisica = copy.deepcopy(pessoa_fisica)
    copia_pessoa_fisica["renda_mensal"] = -1

    controller = PessoaFisicaController(MockPessoaFisicaRepository())

    with pytest.raises(Exception) as error:
        controller.criar(copia_pessoa_fisica)

    assert str(error.value) == "A renda mensal não pode ser negativa."


def test_criar_com_saldo_invalido():
    copia_pessoa_fisica = copy.deepcopy(pessoa_fisica)
    copia_pessoa_fisica["saldo"] = -1

    controller = PessoaFisicaController(MockPessoaFisicaRepository())

    with pytest.raises(Exception) as error:
        controller.criar(copia_pessoa_fisica)

    assert str(error.value) == "O saldo não pode ser negativo."


def test_sacar_dinheiro():
    controller = PessoaFisicaController(MockPessoaFisicaRepository())
    resultado = controller.sacar_dinheiro(1000.0, 1)

    assert resultado == "Saque de R$ 1000.0 realizado com sucesso. Saldo restante: R$ 24000.0"


def test_realizar_extrato():
    controller = PessoaFisicaController(MockPessoaFisicaRepository())
    extrato = controller.realizar_extrato(1)

    assert str(extrato) == "Nome: Pessoa Física Teste, Idade: 22, Saldo: 25000.0"
