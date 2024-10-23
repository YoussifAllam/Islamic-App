# import os
# from .base import * # noqa
from config.env import env


environment = env("ENVIRONMENT")

if environment == "TEST":
    from .test import *  # noqa: F403 F401

    print("\n Django is running in TEST mode", "TEST")

elif environment == "Production":
    from .production import *  # noqa: F403 F401

else:
    from .local import *  # noqa: F403 F401

# Make ENVIRONMENT available as a module-level variable
__all__ = ["environment"]
