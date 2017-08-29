from .common import *
import os

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ADMIN_ENABLED = False

CORS_ORIGIN_WHITELIST = (
    'zachperkitny.com',
)