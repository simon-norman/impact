from .common import *

DEBUG = True

ALLOWED_HOSTS = [os.environ['HOST_IP']]

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carbontracker',
        'USER': 'carbontracker',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '',
    }
}