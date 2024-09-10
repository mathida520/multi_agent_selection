#!/bin/bash
PROJECT_PATH=...

export PYTHONPATH=$PROJECT_PATH

cd $PROJECT_PATH/backend || exit
#source venv/bin/activate
python run.py &

FLASK_PID=$!

cd $PROJECT_PATH/frontend || exit
#npm install
#nvm use 17
npm start &

REACT_PID=$!

read -r -p "Press enter to stop"

kill $FLASK_PID
kill $REACT_PID
