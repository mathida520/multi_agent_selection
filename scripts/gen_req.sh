#!/bin/bash
PROJECT_PATH=...

if ! pip show pipreqs > /dev/null 2>&1; then
    pip install pipreqs
fi

cd $PROJECT_PATH/backend || exit

pipreqs $PROJECT_PATH/backend --force
