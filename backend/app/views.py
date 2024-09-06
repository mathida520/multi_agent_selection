from flask import jsonify

from backend.app.services.generation import fetch_api_responses, get_local_response
from backend.app.services.msg_handler import process_msgs


def request_all_responses(request_json):
    responses = [get_local_response(request_json)] + fetch_api_responses(request_json["messages"])

    return jsonify(process_msgs(responses))
