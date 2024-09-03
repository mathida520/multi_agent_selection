from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有域名访问API


@app.route('/agents', methods=['POST'])
def agents():
    data = request.get_json()
    user_message = data.get('message', '')

    # 处理消息并生成多个AI代理的响应
    response_data = [
        {"agentName": "Agent 1", "message": f"This is a message: {user_message} from Agent 1."},
        {"agentName": "Agent 2", "message": f"This is a message: {user_message} from Agent 2."},
        {"agentName": "Agent 3", "message": f"This is a message: {user_message} from Agent 3."}
    ]

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
