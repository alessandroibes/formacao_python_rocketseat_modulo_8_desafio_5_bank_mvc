from flask import Blueprint, jsonify

from src.errors.error_handler import handle_errors
from src.main.composer.listar_pessoas_fisicas_composer import listar_pessoas_fisicas_composer
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
