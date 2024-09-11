from flask import Blueprint, request

from app.views import request_all_responses_new


chat_bp = Blueprint('chat', __name__)


@chat_bp.route("/chat", methods=["POST"])
def chat():
    return request_all_responses_new(request.get_json())
