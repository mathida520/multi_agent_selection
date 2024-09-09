from flask import Blueprint, request

from backend.app.views import request_all_responses

chat_bp = Blueprint('chat', __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    return request_all_responses(request.get_json())
