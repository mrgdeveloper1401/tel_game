import os
from decouple import config

from django.core.wsgi import get_wsgi_application

debug_mode = config('DEBUG', default=False, cast=bool)

if debug_mode:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tel_game.envs.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tel_game.envs.production')

application = get_wsgi_application()
