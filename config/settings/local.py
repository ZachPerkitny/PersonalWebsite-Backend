from .common import *

SECRET_KEY = '5#q_w-%@-=8e!7(jq45all_%7h_&_*7^e9*3wv&)imzvy%=rq*'
DEBUG = True
ADMIN_ENABLED = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zachperkitny',
        'USER': 'zach',
        'PASSWORD': 'vagrant',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
