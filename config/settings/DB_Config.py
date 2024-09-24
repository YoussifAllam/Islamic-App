# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

from config.env import BASE_DIR
from os.path import join
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  join(BASE_DIR, 'db.sqlite3'),
    }
}
