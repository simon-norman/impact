from .common import *

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1"
]

SECRET_KEY = '8vuimd0-*^^w26hvq9!9s8o5gj*)*24s+r+w#2xhfjj+&ozw^b'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carbontracker',
        'USER': 'carbontracker',
        'PASSWORD': 'simon',
        'HOST': 'localhost',
        'PORT': '',
    }
}