from pydantic import BaseModel, field_validator, ValidationError
from pydantic_core import InitErrorDetails

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest


def sacar_dinheiro_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        quantia: float

        @field_validator("quantia")
        @classmethod
        def validar_celular(cls, v):
            if v <= 0:
                error_message = "A quantia para o saque deve ser maior que 0."
                raise ValidationError.from_exception_data(
                    title="invalid_value",
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
