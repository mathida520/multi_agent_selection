from flask import Flask
from flask_cors import CORS

from .routes import api_bp


def create_app() -> Flask:
    flask_app = Flask(__name__)
    CORS(flask_app)
    # CORS(flask_app, resources={r"/api/*": {"origins": "http://18.140.117.184:11436"}})

    flask_app.register_blueprint(api_bp)

    return flask_app
