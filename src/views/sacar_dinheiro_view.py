from src.controllers.interfaces.sacar_dinheiro_controller import (
    SacarDinheiroControllerInterface
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.validators.sacar_dinheiro_validator import sacar_dinheiro_validator
from .interfaces.view_interface import ViewInterface


class SacarDinheiroView(ViewInterface):
    def __init__(self, controller: SacarDinheiroControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        sacar_dinheiro_validator(http_request)

        id_pessoa = http_request.params["id_pessoa"]
        quantia = http_request.body["quantia"]
        body_response = self.__controller.sacar_dinheiro(quantia, id_pessoa)

        return HttpResponse(status_code=200, body=body_response)
