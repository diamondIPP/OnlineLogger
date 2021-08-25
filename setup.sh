#!/bin/sh

# remove migrations and the database
if [ -f logger/migrations ]; then rm logger/migrations -r; fi
if [ -f db.sqlite3 ]; then rm db.sqlite3 -r; fi

./manage.py makemigrations logger
./manage.py migrate
./manage.py createsuperuser
