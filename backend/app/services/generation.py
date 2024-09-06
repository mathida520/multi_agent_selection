from typing import List, Dict
import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import OpenAI

# from backend.configs import tools

API_CONFIG_PATH = os.getenv('API_CONFIG_PATH')
LOCAL_CHAT_URL = os.getenv('LOCAL_CHAT_URL')


def get_local_response(request_json: Dict) -> Dict:
    # tool_choice = request_json["tool_choice"]

    _request_json = {
        "model": "llama3.1",
        "messages": request_json["messages"],
        "stream": False,
        "options": {
            "seed": 101,
            "temperature": 0
        },
        # "tools": [tool_choice] if tool_choice else request_json.get("tools", tools)
    }
    response = requests.post(
        LOCAL_CHAT_URL,
        headers={"Content-Type": "application/json"},
        json=_request_json
    )

    return response.json()


def fetch_api_response(model, api_key, base_url, msgs) -> Dict:
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    completion = client.chat.completions.create(
        model=model,
        messages=msgs,
    )
    return {
        'model': model,
        'response': completion.to_dict()
    }


def fetch_api_responses(msgs: List[Dict]) -> List[Dict]:
    responses = []

    with open(API_CONFIG_PATH, 'r') as file:  # todo
        models = json.load(file)

    with ThreadPoolExecutor(max_workers=len(models)) as executor:
        future_to_model = {
            executor.submit(fetch_api_response, model, api_info['api_key'], api_info['base_url'], msgs): model
            for model, api_info in models.items()
        }
        for future in as_completed(future_to_model):
            responses.append(future.result())

    return responses
