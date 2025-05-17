from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.composer.listar_pessoas_juridicas_composer import listar_pessoas_juridicas_composer
from src.main.composer.criar_pessoa_juridica_composer import criar_pessoa_juridica_composer
from src.views.http_types.http_request import HttpRequest


pessoa_juridica_route_bp = Blueprint("pessoa_juridica_routes", __name__)

@pessoa_juridica_route_bp.route("/pessoas_juridicas", methods=["GET"])
def listar_pessoas_juridicas():
    try:
        http_request = HttpRequest()
        view = listar_pessoas_juridicas_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@pessoa_juridica_route_bp.route("/pessoas_juridicas", methods=["POST"])
def criar_pessoa_juridica():
    try:
        http_request = HttpRequest(body=request.json)
        view = criar_pessoa_juridica_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
