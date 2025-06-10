from tel_game.settings import *

SECRET_KEY = 'django-insecure-hq8!6adaaji@wyl6_7b*#ebqxp^=c7kjj&urek+0acrvle=i@7'

ALLOWED_HOSTS = []


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
