from .base import *
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/environment.json') as file:
    data = json.load(file)
    environment = data["environment"]
    secret_key = data["secret_key"]
    production_database_name = data["production_database_name"]
    production_database_user = data["production_database_user"]
    production_database_password = data["production_database_password"]
    production_database_host = data["production_database_host"]
    email_host = data["email_host"]
    email_port = data["email_port"]
    email_host_user = data["email_host_user"]
    email_host_password = data["email_host_password"]



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ORIGIN_WHITELIST = ('lesson.ninja', 'https://lesson.ninja')

ALLOWED_HOSTS = ["api.lesson.ninja"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': production_database_name,
        'USER': production_database_user,
        'PASSWORD': production_database_password,
        'HOST': production_database_host,
        'PORT': '5432',
    }
}


EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = email_host
EMAIL_PORT = email_port
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
EMAIL_USE_TLS = True