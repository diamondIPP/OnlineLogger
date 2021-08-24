#!/bin/bash

read -ra IP <<< "$(hostname -I)"
LOGGER_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd "$LOGGER_DIR" || exit
if  [ ! -f db.sqlite3 ]; then ./setup.sh; fi

if [[ $(tmux ls) == *"logger"* ]]; then tmux kill-session -t logger; fi
tmux new -d -s logger "./manage.py runserver ${IP[0]}:8000"
