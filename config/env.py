import environ
from django.core.exceptions import ImproperlyConfigured
from os.path import join
env = environ.Env()

BASE_DIR = environ.Path(__file__) - 2
APPS_DIR = BASE_DIR.path("Bidding_and_Compare\apps")

env.read_env(env.str('ENV_PATH', default=join(BASE_DIR, '.env')))

def env_to_enum(enum_cls, value):
    for x in enum_cls:
        if x.value == value:
            return x

    raise ImproperlyConfigured(f"Env value {repr(value)} could not be found in {repr(enum_cls)}")
