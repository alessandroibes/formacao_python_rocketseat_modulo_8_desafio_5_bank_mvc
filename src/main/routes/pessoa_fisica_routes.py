from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.composer.listar_pessoas_fisicas_composer import listar_pessoas_fisicas_composer
from src.main.composer.criar_pessoa_fisica_composer import criar_pessoa_fisica_composer
from src.main.composer.consultar_saldo_pessoa_fisica_composer import (
    consultar_saldo_pessoa_fisica_composer
)
from src.main.composer.realizar_extrato_pessoa_fisica_composer import (
    realizar_extrato_pessoa_fisica_composer
)
from src.views.http_types.http_request import HttpRequest


pessoa_fisica_route_bp = Blueprint("pessoa_fisica_routes", __name__)

@pessoa_fisica_route_bp.route("/pessoas_fisicas", methods=["GET"])
def listar_pessoas_fisicas():
    try:
        http_request = HttpRequest()
        view = listar_pessoas_fisicas_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@pessoa_fisica_route_bp.route("/pessoas_fisicas", methods=["POST"])
def criar_pessoa_fisica():
    try:
        http_request = HttpRequest(body=request.json)
        view = criar_pessoa_fisica_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@pessoa_fisica_route_bp.route("/pessoas_fisicas/<id_pessoa>/saldo", methods=["GET"])
def consultar_saldo_pessoa_fisica(id_pessoa):
    try:
        http_request = HttpRequest(params={ "id_pessoa": id_pessoa })
        view = consultar_saldo_pessoa_fisica_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@pessoa_fisica_route_bp.route("/pessoas_fisicas/<id_pessoa>/extrato", methods=["GET"])
def realizar_extrato_pessoa_fisica(id_pessoa):
    try:
        http_request = HttpRequest(params={ "id_pessoa": id_pessoa })
        view = realizar_extrato_pessoa_fisica_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
