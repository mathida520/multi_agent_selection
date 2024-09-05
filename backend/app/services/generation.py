import json
import requests

from openai import OpenAI

from backend.configs import tools


def get_local_response(request_json):
    tool_choice = request_json["tool_choice"]

    _request_json = {
        "model": "llama3.1",
        "messages": request_json["messages"],
        "stream": request_json["stream"],
        "options": {
            "seed": 101,
            "temperature": 0
        },
        "tools": [tool_choice] if tool_choice else request_json.get("tools", tools)
    }

    response = requests.post(
        "http://localhost:11434/api/chat",
        headers={"Content-Type": "application/json"},
        json=_request_json
    )

    return response.json()

    
def fetch_api_responses(msgs):
    responses = []

    with open('../../configs/api.json', 'r') as file:
        models = json.load(file)

    for model, config in models.items():
        client = OpenAI(
            api_key=config['api_key'],
            base_url=config['base_url'],
        )
        completion = client.chat.completions.create(
            model=model,
            messages=msgs,
        )
        responses.append({
            'model': model,
            'response': completion.to_dict()
        })

    return responses
