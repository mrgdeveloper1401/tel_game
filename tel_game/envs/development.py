from tel_game.settings import *

SECRET_KEY = 'django-insecure-hq8!6adaaji@wyl6_7b*#ebqxp^=c7kjj&urek+0acrvle=i@7'

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    "debug_toolbar"
]

INTERNAL_IPS = [
    "127.0.0.1"
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'telgamedb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5433',
        'CONN_MAX_AGE': 300,
    }
}

CACHES['default']["LOCATION"] = "redis://127.0.0.1:6380/9"
