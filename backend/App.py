from flask import Flask, request, jsonify
import requests
from Tools import tools, Tools
from flask_cors import CORS

Tools = Tools()

app = Flask(__name__)
CORS(app)  # 允许所有域名访问API


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

    url = "http://localhost:11434/api/chat"
    response = requests.post(url, headers=headers, json=data)

    response_json = response.json()
    formatted_data = extract_and_format_response(response_json)
    return jsonify(formatted_data)
    # return response.text
    # return data


def extract_and_format_response(response_json):
    """
    Extracts and formats the response to include model, message, and color.

    Parameters:
    response_json (dict): The JSON response from the chat completion request.

    Returns:
    list: A list of formatted dictionaries with 'model', 'message', and 'color'.
    """
    model = response_json.get("model", "Agent 1")  # Default to "Agent 1" if no model is provided
    content = response_json.get("message", {}).get("content", "")

    if not content:
        content = "error"

    # Get the color for the model or default to a specific color
    color = "#3498db"  # Default color if model not in predefined models

    # Return the structured response as a list (even if it's just one element)
    return [{
        "model": model,
        "message": content,
        "color": color
    }]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=11435)
