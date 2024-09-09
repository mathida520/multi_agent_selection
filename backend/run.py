# import os
# from urllib.parse import urlparse

from dotenv import load_dotenv

from backend.app import create_app


if __name__ == "__main__":
    load_dotenv()
    # port = urlparse(os.getenv('REACT_APP_BACK_URL_1')).port
    port = 11435

    flask_app = create_app()
    flask_app.run(debug=True, host='0.0.0.0', port=port)
  
# sudo lsof -i :11435
# sudo kill -9

# ps aux | grep gunicorn
# gunicorn -w 4 -b 0.0.0.0:11435 'backend.wsgi:create_app()'
# pkill gunicorn