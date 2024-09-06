import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

class Tools:
    def __init__(self) -> None:
        with open(r"./api.json", 'r') as file:
            self.data = json.load(file)

    # send request
    def send_request(self, agent, details, message):
        payload = details["payload"]
        payload["text"] = message
        headers = {
            "Authorization": f"Bearer {details['key']}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(details["url"], json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                return agent, response.json()
            else:
                return agent, {"error": f"Failed with status code {response.status_code}"}
        except requests.Timeout:
            return agent, {"error": "Request timed out"}
        except requests.RequestException as e:
            return agent, {"error": str(e)}
    
    # find image
    def find_image_in_json(self, json_data):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == "image":
                    return value
                if isinstance(value, (dict, list)):
                    result = self.find_image_in_json(value)
                    if result:
                        return result
        elif isinstance(json_data, list):
            for item in json_data:
                result = self.find_image_in_json(item)
                if result:
                    return result
        return None

    # send request to third pairty api. Conurrently
    def picture_generation(self, message: str):
        results = []
        with ThreadPoolExecutor(max_workers=len(self.data)) as executor:
            future_to_agent = {
                executor.submit(self.send_request, agent, details, message) : agent for agent, details in self.data.items()
            }

            for future in as_completed(future_to_agent):
                agent = future_to_agent[future]
                try:
                    agent, result = future.result()
                    image_data = self.find_image_in_json(result)
                    entry = {
                        "agentName": agent,
                        "message": message,
                        "image": image_data if image_data else []
                    }
                    results.append(entry)
                except Exception as e:
                    results.append({
                        "agentName": agent,
                        "message": message,
                        "image": [],
                        "error": str(e)
                    })
        
        return results
    



    def dev_pic_generation(self, ):
        data = [
            {
                "agentName": "Agent 1",
                "message": "This is the first message from Agent 1.",
                "image": []
            },
            {
                "agentName": "Agent 2",
                "message": "This is a message from Agent 2.",
                "image": []
            },
            {
                "agentName": "Agent 3",
                "message": "This is a message from Agent 3.",
                "image": []
            }
        ]

# tools for LLama3.1
# TODO: seperate it in a json file?
tools = [
    {   
        "type": "function",
        "function":{
            "name": "picture_generatin",
            "description": "This is a function used to request thrird party agents/server to generate images based on text provided",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message from user for image generation",
                    },
                },
                
            },
            "required": ["message"]
        }
    },

    {
        "type": "function",
        "function":{
            "name": "identifyTask",
            "description": "Identify the task based on user's input",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message from user for task recognition",
                    },
                    "task": {
                        "type": "string",
                        "enum": ["pictureGeneration", "undefinedTask"],
                        "description": "The supported tasks. AI should choose one task based on user's message.",
                    },
                }
            },
            "required": ["message", "task"]
        }
    }
]

