# pylint: disable=no-self-argument
import re

from pydantic import BaseModel, constr, ValidationError, field_validator
from pydantic_core import InitErrorDetails

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest


def criar_pessoa_juridica_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        faturamento: float
        idade: int
        nome_fantasia: str
        celular: str
        email_corporativo: str
        categoria: constr(min_length=2) # type: ignore
        saldo: float

        @field_validator("nome_fantasia")
        @classmethod
        def validar_nome(cls, v):
            pattern = re.compile(r'^([A-ZÁÉÍÓÚ][a-záéíóú]+(?: [A-ZÁÉÍÓÚ][a-záéíóú]+)+)$')
            if not pattern.match(v):
                error_message = "Nome fantasia inválido."
                raise ValidationError.from_exception_data(
                    title="invalid_name",
                    line_errors=[
                        InitErrorDetails(
                            {
                                "type": "value_error",
                                "input": v,
                                "ctx": {
                                    "error": error_message,
                                },
                            }
                        )
                    ]
                )
            return v

        @field_validator("celular")
        @classmethod
        def validar_celular(cls, v):
            # Exemplo: formato brasileiro +5511912345678
            pattern = re.compile(r'^\+55\d{2}9\d{8}$')
            if not pattern.match(v):
                error_message = "Número de celular inválido. Use o formato +5511999999999"
                raise ValidationError.from_exception_data(
                    title="invalid_name",
                    line_errors=[
                        InitErrorDetails(
                            {
                                "type": "value_error",
                                "input": v,
                                "ctx": {
                                    "error": error_message,
                                },
                            }
                        )
                    ]
                )
            return v

        @field_validator('email_corporativo')
        @classmethod
        def validar_email(cls, v):
            # Regex básica para e-mails válidos
            pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not pattern.match(v):
                error_message = "Endereço de e-mail inválido."
                raise ValidationError.from_exception_data(
                    title="invalid_name",
                    line_errors=[
                        InitErrorDetails(
                            {
                                "type": "value_error",
                                "input": v,
                                "ctx": {
                                    "error": error_message,
                                },
                            }
                        )
                    ]
                )
            return v

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
