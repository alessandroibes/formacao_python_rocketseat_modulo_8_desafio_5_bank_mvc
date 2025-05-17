from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.criar_pessoa_juridica_controller import CriarPessoaJuridicaController
from src.views.criar_pessoa_juridica_view import CriarPessoaJuridicaView


def criar_pessoa_juridica_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = CriarPessoaJuridicaController(model)
    view = CriarPessoaJuridicaView(controller)

    return view
