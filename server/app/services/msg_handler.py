from typing import List, Dict

import random


def process_msgs(responses: List[Dict]) -> List[Dict]:
    msgs = []
    colors = ["#B5D9FE", "#F9C2C2", "#FFE195"]

    for response in responses:
        model = response.get("model", "")
        color = random.choice(colors)
        if model == "llama3.1":
            msgs.append({
                "model": model,
                "message": response.get("message", {}).get("content", ""),
                'images': response.get('images', []),
                "color": color
            })
        else:
            msgs.append({
                'model': model,
                'message': response.get('response', {}).get('choices', [{}])[0].get('message', {}).get('content', ""),
                'images': response.get('response', {}).get('choices', [{}])[0].get('images', []),
                'color': color,
            })
    return msgs
