from src.controllers.criar_pessoa_juridica_controller import CriarPessoaJuridicaController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.validators.criar_pessoa_juridica_validator import criar_pessoa_juridica_validator
from .interfaces.view_interface import ViewInterface


class CriarPessoaJuridicaView(ViewInterface):
    def __init__(self, controller: CriarPessoaJuridicaController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        criar_pessoa_juridica_validator(http_request)

        request_data = http_request.body
        body_response = self.__controller.criar(request_data)

        return HttpResponse(status_code=201, body=body_response)
