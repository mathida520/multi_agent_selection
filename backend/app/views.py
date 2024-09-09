from flask import jsonify

from backend.app.services.generation import Generation
from backend.app.services.msg_handler import process_msgs

from backend.app.services.ConfigLoader import ConfigLoader
config = ConfigLoader()

generation = Generation(config('API_CONFIG_PATH'), config('LOCAL_CHAT_URL'))
def request_all_responses(request_json):
    responses = [generation.get_local_response(request_json)] + generation.fetch_api_responses(request_json["messages"])

    return jsonify(process_msgs(responses))
