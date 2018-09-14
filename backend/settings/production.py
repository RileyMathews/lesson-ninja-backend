from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ORIGIN_WHITELIST = ('lesson.ninja')

ALLOWED_HOSTS = ["api.lesson.ninja"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}