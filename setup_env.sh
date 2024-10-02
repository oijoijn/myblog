if [ "$1" = "r" ]; then
    python manage.py runserver 0.0.0.0:8000
elif [ "$1" = "s" ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py migrate accounts
    python manage.py migrate blog
elif [ "$1" = "c" ]; then
    python manage.py createsuperuser --username rootq --email root@root.com 
fi