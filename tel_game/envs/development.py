from email.policy import default

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

        "OPTIONS": {
            "pool": True,
            # "min_size": config("POOL_MIN_SIZE", default=1, cast=int),
            # "max_size": config("POOL_MAX_SIZE", default=2, cast=int),
            # "timeout": 15,
        }
    }
}

CACHES['default']["LOCATION"] = "redis://127.0.0.1:6380/9"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
