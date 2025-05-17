from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.realizar_extrato_controller import (
    RealizarExtratoController
)
from src.views.realizar_extrato_view import RealizarExtratoView


def realizar_extrato_pessoa_fisica_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = RealizarExtratoController(model)
    view = RealizarExtratoView(controller)

    return view
