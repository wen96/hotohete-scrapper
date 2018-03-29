release: python manage.py migrate --settings=scrapper.production
web: gunicorn scrapper.wsgi --log-file=-