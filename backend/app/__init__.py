from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS

from .routes import chat_bp


def create_app():
    flask_app = Flask(__name__)
    CORS(flask_app)

    flask_app.register_blueprint(chat_bp)

    load_dotenv()
    return flask_app
