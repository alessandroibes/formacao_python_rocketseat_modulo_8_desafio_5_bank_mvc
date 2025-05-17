import copy
import pytest

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .criar_pessoa_juridica_validator import criar_pessoa_juridica_validator


pessoa_juridica = {
    "faturamento": 100000.00,
    "idade": 5,
    "nome_fantasia": "Empresa Teste",
    "celular": "+5511987654321",
    "email_corporativo": "empresa_teste@example.com",
    "categoria": "Categoria Teste",
    "saldo": 250000.00,
}

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_criar_pessoa_juridica_validator():
    request = MockRequest(pessoa_juridica)

    criar_pessoa_juridica_validator(request)


def test_criar_pessoa_juridica_validator_com_nome_completo_invalido():
    pessoa_juridica_invalida = copy.deepcopy(pessoa_juridica)
    pessoa_juridica_invalida["nome_fantasia"] = "Adm"
    request = MockRequest(pessoa_juridica_invalida)

    with pytest.raises(HttpUnprocessableEntityError) as error:
        criar_pessoa_juridica_validator(request)

    assert error.value.message[0]["msg"] == "Value error, Nome fantasia inválido."


def test_criar_pessoa_juridica_validator_com_celular_invalido():
    pessoa_juridica_invalida = copy.deepcopy(pessoa_juridica)
    pessoa_juridica_invalida["celular"] = "1234-5678"
    request = MockRequest(pessoa_juridica_invalida)

    with pytest.raises(HttpUnprocessableEntityError) as error:
        criar_pessoa_juridica_validator(request)

    assert error.value.message[0]["msg"] == \
        "Value error, Número de celular inválido. Use o formato +5511999999999"


def test_criar_pessoa_juridica_validator_com_email_invalido():
    pessoa_juridica_invalida = copy.deepcopy(pessoa_juridica)
    pessoa_juridica_invalida["email_corporativo"] = "teste#teste.com"
    request = MockRequest(pessoa_juridica_invalida)

    with pytest.raises(HttpUnprocessableEntityError) as error:
        criar_pessoa_juridica_validator(request)

    assert error.value.message[0]["msg"] == "Value error, Endereço de e-mail inválido."
