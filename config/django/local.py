from config.env import env

from .base import *  # noqa

DEBUG = env.bool("DJANGO_DEBUG_LOCAL", default=False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
