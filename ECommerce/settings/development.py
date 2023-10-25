from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-5)l8e6*rj(f7)c$ckocgc&2p(4k+(hku8l)p%z(5&b&e$7b@6j'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ECommerce',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/2',
        'TIMEOUT': 20,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}

# # Configuration of the Database created in the pythonanywhere with 
# # DATABASE name =  shivangi21$ECOmmerce
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'shivangi21$ECommerce',
#         'HOST': 'shivangi21.mysql.pythonanywhere-services.com',
#         'USER': 'shivangi21',
#         'PASSWORD': 'password@2001'
#     }
# }

# # CACHE - File system based used to list the Products
# # expire in 1 minutes
# CACHES = {
# 'default': {
#     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#     'LOCATION': '/var/tmp/django_cache',
#     'TIMEOUT': 60,
#   }
# }