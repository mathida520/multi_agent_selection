#!/bin/bash
CODE_PATH=/home/ec2-user/dev

export PYTHONPATH=$CODE_PATH

cd $CODE_PATH/backend || exit
#source venv/bin/activate
gunicorn -w 4 -b 0.0.0.0:11435 'backend.wsgi:create_app()' &

FLASK_PID=$!

cd $CODE_PATH/frontend || exit
npm install
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
nvm use 17
export PORT=11436
npm start &

REACT_PID=$!

# read -r -p "Press enter to stop"

# kill $FLASK_PID
# kill $REACT_PID