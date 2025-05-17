from src.controllers.interfaces.consultar_saldo_pessoa_fisica_controller import (
    ConsultarSaldoPessoaFisicaControllerInterface
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class ConsultarSaldoPessoaFisicaView(ViewInterface):
    def __init__(self, controller: ConsultarSaldoPessoaFisicaControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_pessoa = http_request.params["id_pessoa"]
        body_response = self.__controller.consultar_saldo(id_pessoa)

        return HttpResponse(status_code=200, body=body_response)
