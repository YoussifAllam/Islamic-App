from config.env import env, BASE_DIR
from os.path import join
from .base import *  # noqa

UPPER_DIR = BASE_DIR.parent
DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": join(UPPER_DIR, "db.sqlite3"),
    }
}


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    "IS_RUNNING_TESTS": False,
}

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',
    'http://localhost'
]
