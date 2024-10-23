CACHEOPS = {
    "Products.allProductCategories": {
        "ops": "all",  # Cache all operations: get, fetch, etc.
        "timeout": 15 * 60,  # Cache timeout set to 15 minutes
    },
    "Vendors.VendorReviews": {
        "ops": "all",  # Cache all operations: get, fetch, etc.
        "timeout": 15 * 60,  # Cache timeout set to 15 minutes
    },
    "Vendors.VendorBalance": {
        "ops": "all",  # Cache all operations: get, fetch, etc.
        "timeout": 15 * 60,  # Cache timeout set to 15 minutes
    },
    "Orders.OrderDetails": {
        "ops": "all",  # Cache all operations: get, fetch, etc.
        "timeout": 15 * 60,  # Cache timeout set to 15 minutes
    },
}

CACHEOPS_REDIS = {
    "host": "redis",  # Redis endpoint
    "port": 6379,
    "socket_timeout": 3,  # connection timeout in seconds, optional
}
CACHEOPS_DEGRADE_ON_FAILURE = True

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         'LOCATION': 'redis://redis:6379',
#     }
# }
