from flask import Blueprint, request

from .views import gen_primary, gen_auxi
from services.generation import get_local_response

api_bp = Blueprint('api', __name__, url_prefix='/api')


# the very basic interaction
@api_bp.route("/basic/localChat", methods=["POST"])
def generate_localresponse():
    return get_local_response(request.get_json())


@api_bp.route("/gen/prim", methods=["POST"])
def generate_primary():
    return gen_primary(request.get_json())


@api_bp.route("/gen/auxi", methods=["POST"])
def generate_auxiliary():
    return gen_auxi(request.get_json())

@api_bp.route("/test/chat", methods=["POST"])
def test():
    import os
    API_CONFIG_PATH = os.getenv('API_CONFIG_PATH')
    print(API_CONFIG_PATH)
    return "success"

