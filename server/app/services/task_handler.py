import http.client
import json
import os

from RequestHandler import RequestHandler


LOCAL_CHAT_URL = os.getenv('LOCAL_CHAT_URL')

PICTURE_GENERATION= "pictureGeneration"


def task_classification(content):
    payload = json.dumps({
        "model": "llama3.1",
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "stream": False,
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "identifyTask",
                    "description": "Identify the task based on user's input",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string",
                                "description": "The message from user for task recognition"
                            },
                            "task": {
                                "type": "string",
                                "enum": [
                                    PICTURE_GENERATION,
                                    "undefinedTask"
                                ],
                                "description": "The supported tasks. AI should choose one task based on user's message."
                            }
                        },
                        "required": [
                            "message",
                            "task"
                        ]
                    }
                }
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = RequestHandler.post(LOCAL_CHAT_URL, headers, payload, timeout = 10)
    arguments = response["message"]["tool_calls"][0]["function"]["arguments"]
    task = json.loads(arguments)["task"]
    return task
