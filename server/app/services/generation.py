from typing import List, Dict

import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import OpenAI
from openai.lib.azure import AzureOpenAI

from app.services.RequestHandler import RequestHandler
from app.services.task_handler import PICTURE_GENERATION

API_CONFIG_PATH = os.getenv('API_CONFIG_PATH')
LOCAL_CHAT_URL = os.getenv('LOCAL_CHAT_URL')


# todo add function_call
def get_local_response(request_json: Dict, tools: list = []) -> Dict:
    if tools:
        payload = {
            "model": "llama3.1",
            "messages": [
                {
                    "role": "user",
                    "content": request_json.get('message', ''),
                }
            ],
            "stream": False,
            "options": {
                "seed": 101,
                "temperature": 0
            },
            "tools": tools
        }
    else: 
        payload = {
            "model": "llama3.1",
            "messages": request_json.get("message", ""),
            "stream": False,
            "options": {
                "seed": 101,
                "temperature": 0
            },
        }
    response = RequestHandler.post(LOCAL_CHAT_URL, headers={"Content-Type": "application/json"}, json=payload, timeout = 10)
    
    return response


def fetch_api_response(model, api_key, url, option, msgs, task) -> Dict:
    # currently, only 2 missions: {PICTURE_GENERATION, general_chat}
    # the models used for these missions are different, no intersect. So at current stage, we use if else to construct payloads for different missions
    # TODO: encapulate a logic for payload generation based on mission type
    if task == PICTURE_GENERATION:
        payload = {
            "prompt": msgs
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        completion = RequestHandler.post(url, headers=headers, json=payload, timeout=10)
    else:
        if "azure" in model:
            client = AzureOpenAI(
                api_key=api_key,
                api_version=option,
                azure_endpoint=url,
            )
            completion = client.chat.completions.create(
                model=model.replace("azure-", ""),
                messages=msgs,
            ).to_dict()
        else:
            client = OpenAI(
                api_key=api_key,
                base_url=url,
            )
            completion = client.chat.completions.create(
                model=model,
                messages=msgs,
            ).to_dict()

    return {
        'model': model,
        'response': completion
    }


def fetch_api_responses(models: Dict, msgs: List[Dict]) -> List[Dict]:
    responses = []

    with ThreadPoolExecutor(max_workers=len(models)) as executor:
        future_to_model = {
            executor.submit(
                fetch_api_response, model, api_info["api_key"], api_info["url"], api_info["option"], msgs
            ): model for model, api_info in models.items()
        }
        for future in as_completed(future_to_model):
            responses.append(future.result())

    return responses
