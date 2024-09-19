from typing import List, Dict

import os
import json
from dotenv import load_dotenv
from .services.generation import fetch_api_responses,  fetch_api_response
from .services.model_handler import get_model_list
from .services.msg_handler import process_msgs, resort_msgs
from .services.ranking import rerank_models, rerank_responses
from .services.task_handler import task_classification
#### 这个鬼地方别动
load_dotenv()
API_CONFIG_PATH = os.path.join(os.getenv('API_CONFIG_PATH'))
#### 这个鬼地方别动


def get_models_dict():
    if API_CONFIG_PATH is None:
        raise ValueError("API_CONFIG_PATH isssss not set")
    with open(API_CONFIG_PATH, 'r') as file:
        models = json.load(file)
    return models


def gen_primary(request_json: Dict):
    num = 2
    models_info = get_models_dict()
    reranked_models_name = rerank_models(list(models_info.keys()))
    name1 = reranked_models_name[: num]

    responses = request_all_responses(
        {key: models_info[key] for key in name1 if key in models_info},
        request_json,
    )

    return {
        "modelsResponse": responses,
        "remainingModels": reranked_models_name[num:]
    }


def gen_auxi(request_json: Dict):
    models_info = get_models_dict()
    model_name = request_json["modelName"]
    model_info = models_info[model_name]
    responses = fetch_api_response(
        model_name,
        model_info["api_key"],
        model_info["url"],
        model_info["option"],
        request_json["messages"]
    )
    responses = process_msgs([responses])
    return responses

# todo 还没有对答案排序
def gen_batch(request_json: Dict):
    models_info = get_models_dict()
    model_names = request_json["modelNames"]
    responses=[]
    for model_name in model_names:
        if model_name not in models_info:
            raise ValueError(f"Model {model_name} not found in models_info")
        else:
            model_info = models_info[model_name]
            response = fetch_api_response(
                model_name,
                model_info["api_key"],
                model_info["url"],
                model_info["option"],
                request_json["messages"]
            )
            responses.append(response)

    responses = resort_msgs(responses,request_json["messages"]["content"])
    return responses




def request_all_responses(models_info: Dict, request_json: Dict):
    responses = fetch_api_responses(models_info, request_json["messages"])
    responses = process_msgs(responses)
    responses = rerank_responses(responses)

    return responses


def task_classify(request_json: Dict):
    content = request_json["messages"][0]["content"]
    return task_classification(content)


def get_models(task_typs):
    return get_model_list(task_typs)