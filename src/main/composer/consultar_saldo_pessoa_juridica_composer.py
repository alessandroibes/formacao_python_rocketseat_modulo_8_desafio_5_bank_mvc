from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.consultar_saldo_pessoa_juridica_controller import (
    ConsultarSaldoPessoaJuridicaController
)
from src.views.consultar_saldo_pessoa_juridica_view import ConsultarSaldoPessoaJuridicaView


def consultar_saldo_pessoa_juridica_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = ConsultarSaldoPessoaJuridicaController(model)
    view = ConsultarSaldoPessoaJuridicaView(controller)

    return view
