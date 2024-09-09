import os
from dotenv import load_dotenv

class ConfigLoader:
    def __init__(self, path: str = "../../configs/.env") -> None:
        self.path = os.path.join(os.path.dirname(__file__), path)
        load_dotenv(dotenv_path=self.path)
        if not os.path.exists(self.path):
            raise FileNotFoundError(f".env file not found at {self.path}")

    def __call__(self, key: str, default_value=None):
        return os.getenv(key, default_value)