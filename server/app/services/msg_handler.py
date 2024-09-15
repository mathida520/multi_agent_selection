from typing import List, Dict

import random


def process_msgs(responses: List[Dict]) -> List[Dict]:
    msgs = []
    colors = ["#B5D9FE", "#F9C2C2", "#FFE195"]

    for response in responses:
        model = response["model"]
        color = random.choice(colors)
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
