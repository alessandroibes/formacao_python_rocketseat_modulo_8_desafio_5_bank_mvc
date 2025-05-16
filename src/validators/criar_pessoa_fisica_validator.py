# pylint: disable=no-self-argument
import re

from pydantic import BaseModel, constr, ValidationError, field_validator

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest


def criar_pessoa_fisica_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        renda_mensal: float
        idade: int
        nome_completo: str
        celular: str
        email: str
        categoria: constr(min_length=2) # type: ignore
        saldo: float

        #^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$

        @field_validator("nome_completo")
        def validar_nome(cls, v):
            pattern = re.compile(r'^([A-ZÁÉÍÓÚ][a-záéíóú]+(?: [A-ZÁÉÍÓÚ][a-záéíóú]+)+)$')
            if not pattern.match(v):
                raise ValueError('Nome completo inválido.')
            return v

        @field_validator("celular")
        def validar_celular(cls, v):
            # Exemplo: formato brasileiro +5511912345678
            pattern = re.compile(r'^\+55\d{2}9\d{8}$')
            if not pattern.match(v):
                raise ValueError('Número de celular inválido. Use o formato +5511999999999')
            return v

        @field_validator('email')
        @classmethod
        def validar_email(cls, v):
            # Regex básica para e-mails válidos
            pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not pattern.match(v):
                raise ValueError('Endereço de e-mail inválido.')
            return v

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
