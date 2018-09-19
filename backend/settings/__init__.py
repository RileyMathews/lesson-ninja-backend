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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

if environment == "development":
    from .development import *
elif environment == "production":
    from .production import *
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
