from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.consultar_saldo_pessoa_fisica_controller import (
    ConsultarSaldoPessoaFisicaController
)
from src.views.consultar_saldo_pessoa_fisica_view import ConsultarSaldoPessoaFisicaView


def consultar_saldo_pessoa_fisica_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = ConsultarSaldoPessoaFisicaController(model)
    view = ConsultarSaldoPessoaFisicaView(controller)

    return view
