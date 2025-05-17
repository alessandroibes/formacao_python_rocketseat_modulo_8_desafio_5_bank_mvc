from src.controllers.interfaces.realizar_extrato_controller import (
    RealizarExtratoControllerInterface
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class RealizarExtratoView(ViewInterface):
    def __init__(self, controller: RealizarExtratoControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_pessoa = http_request.params["id_pessoa"]
        body_response = self.__controller.realizar_extrato(id_pessoa)

        return HttpResponse(status_code=200, body=body_response)
