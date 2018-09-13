import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/environment.json') as file:
    data = json.load(file)
    environment = data["environment"]
    secret_key = data["secret_key"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

if environment == "development":
    from .development import *
elif environment == "production":
    from .production import *
