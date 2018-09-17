from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    'localhost:3000',
    '127.0.0.1:8080',
    '127.0.0.1:3000',
    '127.0.0.1:3001',
    'localhost:3001',
    'lesson.ninja',
)



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'