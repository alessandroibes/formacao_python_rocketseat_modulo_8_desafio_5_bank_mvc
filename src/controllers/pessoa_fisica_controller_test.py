# pylint: disable=unused-argument
import copy
import pytest

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
