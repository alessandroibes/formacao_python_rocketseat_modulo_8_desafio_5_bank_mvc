from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.listar_pessoas_fisicas_controller import ListarPessoasFisicasController
from src.views.listar_pessoas_fisicas_view import ListarPessoasFisicasView


def listar_pessoas_fisicas_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = ListarPessoasFisicasController(model)
    view = ListarPessoasFisicasView(controller)

    return view
