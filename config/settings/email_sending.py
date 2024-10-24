from os import getenv
import logging

# Get an instance of a logger
logger = logging.getLogger("myapp")

EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = int(getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = getenv("EMAIL_USE_TLS") == "True"
EMAIL_USE_SSL = getenv("EMAIL_USE_SSL") == "True"
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_DEBUG = True  # This will log SMTP communication
