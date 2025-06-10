import os

from django.core.asgi import get_asgi_application
from decouple import config


debug_mod = config('DEBUG', cast=bool, default=False)


if debug_mod:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tel_game.envs.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tel_game.envs.production')

application = get_asgi_application()
