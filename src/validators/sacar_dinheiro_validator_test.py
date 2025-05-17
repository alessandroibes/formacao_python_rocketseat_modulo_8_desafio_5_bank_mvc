import pytest

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .sacar_dinheiro_validator import sacar_dinheiro_validator


class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_sacar_dinheiro_validator_pessoa_fisica():
    request = MockRequest({
        "quantia": 10000.0
    })

    sacar_dinheiro_validator(request)


def test_sacar_dinheiro_validator_pessoa_fisica_without_required_field():
    request = MockRequest({})

    with pytest.raises(HttpUnprocessableEntityError) as error:
        sacar_dinheiro_validator(request)

    error_message = "Field required"
    assert error.value.message[0]["msg"] == error_message


def test_sacar_dinheiro_validator_pessoa_fisica_with_invalid_value():
    request = MockRequest({
        "quantia": 0
    })

    with pytest.raises(HttpUnprocessableEntityError) as error:
        sacar_dinheiro_validator(request)

    error_message = "Value error, A quantia para o saque deve ser maior que 0."
    assert error.value.message[0]["msg"] == error_message
