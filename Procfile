init: python manage.py db init
release: python manage.py db upgrade
web: gunicorn wsgi:app --access-logfile=-