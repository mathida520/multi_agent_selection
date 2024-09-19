from flask import Blueprint, request

from .views import gen_primary, gen_auxi

api_bp = Blueprint('api', __name__, url_prefix='/api')


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

