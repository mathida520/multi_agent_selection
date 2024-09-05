import json

from openai import OpenAI


def get_responses(msgs):
    responses = []

    with open('api.json', 'r') as file:
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


def extract_and_format_response(responses):
    msgs = []
    color = '#3498db'

    for response in responses:
        msgs.append({
            'model': response['model'],
            'message': response['response']['choices'][0]['message']['content'],
            'color': color,
        })

    return msgs


# if __name__ == '__main__':
#     messages = [
#         {'role': 'system', 'content': 'You are a helpful assistant.'},
#         {'role': 'user', 'content': '你是谁？'}
#     ]
#     print(extract_and_format_response(get_responses(messages)))
