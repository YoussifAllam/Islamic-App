from config.env import env, BASE_DIR
from os.path import join
from .base import *  # noqa
UPPER_DIR = BASE_DIR.parent
DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [  # noqa
    'debug_toolbar',
]

MIDDLEWARE += [  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  join(BASE_DIR, 'db.sqlite3'),
    }
}


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}
