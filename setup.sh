#!/bin/sh

rm logger/migrations -r
rm db.sqlite3
./manage.py makemigrations logger
./manage.py migrate logger
./manage.py migrate
./manage.py createsuperuser
