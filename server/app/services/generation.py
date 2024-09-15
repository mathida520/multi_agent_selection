from typing import List, Dict

import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import OpenAI
from openai.lib.azure import AzureOpenAI


API_CONFIG_PATH = os.getenv('API_CONFIG_PATH')
LOCAL_CHAT_URL = os.getenv('LOCAL_CHAT_URL')


# todo add function_call
def get_local_response(request_json: Dict) -> Dict:
    payload = {
        "model": "llama3.1",
        "messages": request_json["messages"],
        "stream": False,
        "options": {
            "seed": 101,
            "temperature": 0
        },
    }
    response = requests.post(
        LOCAL_CHAT_URL,
        headers={"Content-Type": "application/json"},
        json=payload
    )

    return response.json()


def fetch_api_response(model, api_key, url, option, msgs) -> Dict:
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
    # completion = {
    #     "id": "zxc",
    #     "object": "chat.completion",
    #     "created": 777,
    #     "model": model,
    #     "choices": [
    #         {
    #             "index": 0,
    #             "finish_reason": "stop",
    #             "message": {"role": "assistant", "content": "Hi!"}
    #         }
    #     ],
    #     "usage": {"completion_tokens": 109, "prompt_tokens": 24, "total_tokens": 133}
    # }
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
