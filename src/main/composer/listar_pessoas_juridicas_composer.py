from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.listar_pessoas_juridicas_controller import ListarPessoasJuridicasController
from src.views.listar_pessoas_juridicas_view import ListarPessoasJuridicasView


def listar_pessoas_juridicas_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = ListarPessoasJuridicasController(model)
    view = ListarPessoasJuridicasView(controller)

    return view
