from dotenv import load_dotenv
from app import create_app

load_dotenv()
flask_app = create_app()

if __name__ == "__main__":
    port = 11435
    flask_app.run(debug=True, host='0.0.0.0', port=port)


# sudo lsof -i :11435
# nohup gunicorn -w 4 -b 0.0.0.0:11435 server.run:flask_app > outputApi.log 2>&1 &
# curl -X POST http://18.140.117.184:11435/api/test/chat
# nohup npm start > output.log 2>&1 &
# killall gunicorn
# nvm alias default 17