from src.controllers.criar_pessoa_fisica_controller import CriarPessoaFisicaController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class CriarPessoaFisicaView(ViewInterface):
    def __init__(self, controller: CriarPessoaFisicaController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        request_data = http_request.body
        body_response = self.__controller.criar(request_data)

        return HttpResponse(status_code=201, body=body_response)
