if [ "$1" = "r" ]; then
    python manage.py runserver 0.0.0.0:8000
elif [ "$2" = "s" ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py migrate accounts
fi