from typing import List, Dict


def process_msgs(responses: List[Dict]) -> List[Dict]:
    msgs = []
    color = '#3498db'  # todo random

    for response in responses:
        model = response["model"]
        if model == "llama3.1":
            msgs.append({
                "model": model,
                "message": response["message"]["content"],
                "color": color
            })
        else:
            msgs.append({
                'model': model,
                'message': response['response']['choices'][0]['message']['content'],
                'color': color,
            })
    return msgs
