#!/bin/sh

python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
gunicorn tel_game.wsgi -b 0.0.0.0:8000 -w 3
