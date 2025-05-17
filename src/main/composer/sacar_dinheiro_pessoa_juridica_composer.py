from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.sacar_dinheiro_controller import (
    SacarDinheiroController
)
from src.views.sacar_dinheiro_view import SacarDinheiroView


def sacar_dinheiro_pessoa_juridica_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = SacarDinheiroController(model)
    view = SacarDinheiroView(controller)

    return view
