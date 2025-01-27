from .common import *
import os

ALLOWED_HOSTS = ['.zachperkitny.com']
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(http?://)?(\w+\.)?zachperkitny\.com$',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT']
    }
}
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
