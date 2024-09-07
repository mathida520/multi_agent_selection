#!/bin/bash
CODE_PATH=...

export PYTHONPATH=$CODE_PATH

cd $CODE_PATH/backend || exit
#source venv/bin/activate
python run.py &

FLASK_PID=$!

cd $CODE_PATH/frontend || exit
#npm install
npm start &

REACT_PID=$!

read -r -p "Press enter to stop"

kill $FLASK_PID
kill $REACT_PID
