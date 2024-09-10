import os
import json

from flask import jsonify

from backend.app.services.generation import fetch_api_responses, get_local_response
from backend.app.services.msg_handler import process_msgs
from backend.app.services.ranking import rerank_models, rerank_responses

API_CONFIG_PATH = os.getenv('API_CONFIG_PATH')


def get_models_dict():
    with open(API_CONFIG_PATH, 'r') as file:  # todo
        models = json.load(file)

    return models


def request_all_responses_old(request_json):
    models = get_models_dict()
    responses = [get_local_response(request_json)] + fetch_api_responses(models, request_json["messages"])

    return jsonify(process_msgs(responses))


def request_all_responses_new(request_json):
    models = get_models_dict()
    models = rerank_models(models)

    responses = fetch_api_responses(models, request_json["messages"])
    responses = process_msgs(responses)
    responses = rerank_responses(responses)

    return jsonify(responses)
