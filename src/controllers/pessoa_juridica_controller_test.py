# pylint: disable=unused-argument
import copy
import pytest

from .pessoa_juridica_controller import PessoaJuridicaController


pessoa_juridica = {
        "faturamento": 100000.00,
        "idade": 5,
        "nome_fantasia": "Empresa Teste",
        "celular": "8765-4321",
        "email_corporativo": "empresa_teste@example.com",
        "categoria": "Categoria Teste",
        "saldo": 250000.00,
    }


class MockPessoaJuridicaRepository():
    def criar_pessoa_juridica(self, *args, **kwargs) -> None:
        return None


def test_criar():
    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    response = controller.criar(pessoa_juridica)

    assert response["data"]["type"] == "Pessoa Jurídica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_juridica


def test_criar_com_nome_completo_invalido():
    copia_pessoa_juridica = copy.deepcopy(pessoa_juridica)
    copia_pessoa_juridica["nome_fantasia"] = "NomeInválido123"

    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())

    with pytest.raises(Exception) as error:
        controller.criar(copia_pessoa_juridica)

    assert str(error.value) == "Nome da empresa inválido."


def test_criar_com_faturamento_invalido():
    copia_pessoa_juridica = copy.deepcopy(pessoa_juridica)
    copia_pessoa_juridica["faturamento"] = -1

    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())

    with pytest.raises(Exception) as error:
        controller.criar(copia_pessoa_juridica)

    assert str(error.value) == "O faturamento não pode ser negativo."


def test_criar_com_saldo_invalido():
    copia_pessoa_juridica = copy.deepcopy(pessoa_juridica)
    copia_pessoa_juridica["saldo"] = -1

    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())

    with pytest.raises(Exception) as error:
        controller.criar(copia_pessoa_juridica)

    assert str(error.value) == "O saldo não pode ser negativo."
