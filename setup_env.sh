#!/bin/bash
if [ "$1" = "r" ]; then
    python manage.py runserver 0.0.0.0:8000
elif [ "$1" = "s" ]; then
    python manage.py makemigrations
    python manage.py makemigrations accounts
    python manage.py makemigrations blog
    python manage.py migrate
    python manage.py migrate accounts
    python manage.py migrate blog
elif [ "$1" = "rms" ]; then
    rm -rf db.sqlite3
    rm -rf accounts/migrations/
    rm -rf blog/migrations/
elif [ "$1" = "c" ]; then
    python manage.py createsuperuser
elif [ "$1" = "cc" ]; then
    python manage.py collectstatic
fi
