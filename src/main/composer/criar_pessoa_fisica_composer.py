from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.criar_pessoa_fisica_controller import CriarPessoaFisicaController
from src.views.criar_pessoa_fisica_view import CriarPessoaFisicaView


def criar_pessoa_fisica_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = CriarPessoaFisicaController(model)
    view = CriarPessoaFisicaView(controller)

    return view
