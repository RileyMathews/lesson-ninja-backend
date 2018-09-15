from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ORIGIN_WHITELIST = ('lesson.ninja')

ALLOWED_HOSTS = ["api.lesson.ninja"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lessonninja',
        'USER': 'rileymathews',
        'PASSWORD': 'nerdrage132',
        'HOST': 'localhost',
        'PORT': '',
    }
}