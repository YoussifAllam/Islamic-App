# import os
# from .base import * # noqa
import socket


def get_host_name() -> str:
    return socket.gethostname()


current_host = get_host_name()


if current_host == 'test machine name':
    ENVIRONMENT = 'Test'
    from .test import *  # noqa: F403 F401

elif current_host == 'production_server_name':
    ENVIRONMENT = 'Production'
    from .production import *  # noqa: F403 F401

else:
    ENVIRONMENT = 'Local'
    from .local import *  # noqa: F403 F401 # Default to local if unsure

# Make ENVIRONMENT available as a module-level variable
__all__ = ['ENVIRONMENT']
