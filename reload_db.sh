#!/bin/sh

rm logger/migrations -r
rm db.sqlite3
python2 manage.py makemigrations logger
python2 manage.py migrate logger
python2 manage.py migrate
python2 manage.py createsuperuser
