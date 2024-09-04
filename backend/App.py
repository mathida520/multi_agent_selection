from flask import Flask, request, jsonify
import requests
from Tools import tools, Tools
import json



Tools = Tools()

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chatCompletionRequest():
    data = request.json
    messages = data.get("messages")
    tools_data = data.get("tools", tools)
    tool_choice = data.get("tool_choice", [])
    model = data.get("model", "llama3.1")
    stream = data.get("stream", False)

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages,
        "stream": stream,
        "options": {
            "seed": 101,
            "temperature": 0
        }
    }
    data["tools"] = [tool_choice] if tool_choice else tools_data

    url = f"http://localhost:11434/api/chat"
    response = requests.post(url, headers=headers, json=data)
    
    return response.text
    # return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=11435)
