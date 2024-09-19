#!/bin/bash
PROJECT_PATH=/Users/ronglong/PycharmProjects/mutil-agent-selection

export PYTHONPATH=$PROJECT_PATH

cd $PROJECT_PATH/server || exit
#source venv/bin/activate
python run.py &

FLASK_PID=$!

cd $PROJECT_PATH || exit
#npm install
#nvm use 17
npm start &

REACT_PID=$!

read -r -p "Press enter to stop"

kill $FLASK_PID
kill $REACT_PID
