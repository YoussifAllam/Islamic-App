from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
UPPER_DIR = BASE_DIR.parent

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(UPPER_DIR, "debug.log"),
            "formatter": "verbose",
        },
    },

    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",  # Set this to INFO to prevent DEBUG messages
            "propagate": True,
        },
        "myapp": {  # Replace 'myapp' with your app name
            "handlers": ["console", "file"],
            "level": "INFO",  # Set this to INFO to prevent DEBUG messages
            "propagate": True,
        }

    },
}
