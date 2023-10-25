from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-5)l8e6*rj(f7)c$ckocgc&2p(4k+(hku8l)p%z(5&b&e$7b@6j'

ALLOWED_HOSTS = ['127.0.0.1']

#************************* Docker compose command Config ********************

# Docker compose command stop the mysql server in the Local system
# sudo service mysql stop
# sudo systemctl stop mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ECommerce',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}

# configuring the redis cache 
# docker compose command run with above command
# Caching timeout in 20 seconds | modify it
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

CACHES_TTL = 20

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}

#************ use loacl system to run manage.py ******************

# Configure the database on the local system
# sudo service mysql start
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ECommerce',
#         'HOST': 'loaclhost',
#         'USER': 'root',
#         'PASSWORD': 'password'
#     }
# }

# configuring the redis cache 
# run the docker run -d -p 6379:6379 redis (separate) in other terminal
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/2',
#         'TIMEOUT': 20,
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }