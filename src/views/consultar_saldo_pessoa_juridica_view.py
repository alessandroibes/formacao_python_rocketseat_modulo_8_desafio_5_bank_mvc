from src.controllers.interfaces.consultar_saldo_pessoa_juridica_controller import (
    ConsultarSaldoPessoaJuridicaControllerInterface
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class ConsultarSaldoPessoaJuridicaView(ViewInterface):
    def __init__(self, controller: ConsultarSaldoPessoaJuridicaControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_pessoa = http_request.params["id_pessoa"]
        body_response = self.__controller.consultar_saldo(id_pessoa)

        return HttpResponse(status_code=200, body=body_response)
