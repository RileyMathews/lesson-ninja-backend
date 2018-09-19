from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ORIGIN_WHITELIST = ('lesson.ninja', 'https://lesson.ninja')

ALLOWED_HOSTS = ["api.lesson.ninja"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases



EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.mail.us-east-1.awsapps.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@lesson.ninja'
EMAIL_HOST_PASSWORD = 'Di!G3QCt66iLVA'
EMAIL_USE_TLS = True