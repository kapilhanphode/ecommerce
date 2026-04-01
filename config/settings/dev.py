from .base import *
from decouple import config

DEBUG = True
# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')