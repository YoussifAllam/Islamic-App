import os
from .base import *  # noqa
from config.env import env

# This is extremely "eye-poking",
# but we need it, if we want to ignore the debug toolbar in tests
# This is needed because of the way we setup Django Debug Toolbar.
# Since we import base settings, the entire setup will be done, before we have any chance to change.
# A different way of approaching this would be to have a separate set of env variables for tests.
# os.environ.setdefault("DEBUG_TOOLBAR_ENABLED", "False")


SECRET_KEY = env("SECRET_KEY")
DEBUG = True
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST", default=[])

AUTH_PASSWORD_VALIDATORS: list[dict[str, int]] = [  # type: ignore
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE"),
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    },
    "OPTIONS": {
        "options": "-c search_path=public",
    },
    "CONN_MAX_AGE": 60,
    "CONN_HEALTH_CHECKS": True,
}
