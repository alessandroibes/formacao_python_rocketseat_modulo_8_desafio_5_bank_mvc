import copy
import pytest

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .criar_pessoa_fisica_validator import criar_pessoa_fisica_validator


pessoa_fisica = {
    "renda_mensal": 10000.00,
    "idade": 22,
    "nome_completo": "Pessoa Física Teste",
    "celular": "+5585988001260",
    "email": "pfisica@example.com",
    "categoria": "Categoria Teste",
    "saldo": 25000.00,
}


class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_criar_pessoa_fisica_validator():
    request = MockRequest(pessoa_fisica)

    criar_pessoa_fisica_validator(request)


def test_criar_pessoa_fisica_validator_com_nome_completo_invalido():
    pessoa_fisica_invalida = copy.deepcopy(pessoa_fisica)
    pessoa_fisica_invalida["nome_completo"] = "Adm"
    request = MockRequest(pessoa_fisica_invalida)

    with pytest.raises(HttpUnprocessableEntityError) as error:
        criar_pessoa_fisica_validator(request)

    assert error.value.message[0]["msg"] == "Value error, Nome completo inválido."


def test_criar_pessoa_fisica_validator_com_celular_invalido():
    pessoa_fisica_invalida = copy.deepcopy(pessoa_fisica)
    pessoa_fisica_invalida["celular"] = "1234-5678"
    request = MockRequest(pessoa_fisica_invalida)

    with pytest.raises(HttpUnprocessableEntityError) as error:
        criar_pessoa_fisica_validator(request)

    assert error.value.message[0]["msg"] == \
        "Value error, Número de celular inválido. Use o formato +5511999999999"


def test_criar_pessoa_fisica_validator_com_email_invalido():
    pessoa_fisica_invalida = copy.deepcopy(pessoa_fisica)
    pessoa_fisica_invalida["email"] = "teste#teste.com"
    request = MockRequest(pessoa_fisica_invalida)

    with pytest.raises(HttpUnprocessableEntityError) as error:
        criar_pessoa_fisica_validator(request)

    assert error.value.message[0]["msg"] == "Value error, Endereço de e-mail inválido."
