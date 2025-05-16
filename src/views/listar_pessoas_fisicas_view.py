from src.controllers.interfaces.listar_pessoas_fisicas_controller import (
    ListarPessoasFisicasControllerInterface
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class ListarPessoasFisicasView(ViewInterface):
    def __init__(self, controller: ListarPessoasFisicasControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.listar_pessoas_fisicas()
        return HttpResponse(status_code=200, body=body_response)
