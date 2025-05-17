from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.realizar_extrato_controller import (
    RealizarExtratoController
)
from src.views.realizar_extrato_view import RealizarExtratoView


def realizar_extrato_pessoa_juridica_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = RealizarExtratoController(model)
    view = RealizarExtratoView(controller)

    return view
