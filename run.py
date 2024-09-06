import os
from urllib.parse import urlparse
import subprocess

from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    port = urlparse(os.getenv('REACT_APP_BACK_URL_1')).port
    
    code_str = f"""from backend.app import create_app
flask_app = create_app()
flask_app.run(debug=True, host='0.0.0.0', port={port})"""
    subprocess.Popen(['python', '-c', code_str])
    subprocess.Popen(["npm", "start"], cwd='frontend')

    input()
