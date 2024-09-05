from flask import request, jsonify

from .services.generation import fetch_api_responses, get_local_response
from .services.msg_handler import process_msgs

from . import flask_app


@flask_app.route("/chat", methods=["POST"])
def chat():
    request_json = request.get_json()
    api_responses = process_msgs(fetch_api_responses(request_json.get("messages")))
    return jsonify(
        process_msgs(
            api_responses.append(get_local_response(request_json))
        )
    )
