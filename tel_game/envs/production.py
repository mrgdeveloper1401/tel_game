from tel_game.settings import *

from django.utils import timezone

SECRET_KEY = config("PROD_SECRET_KEY", cast=str, default="test<KEY>")

ALLOWED_HOSTS = ''.join(config('ALLOWED_HOSTS', cast=list, default='localhost')).split(",")

MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware",)
MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("TEL_GAME_POSTDB_NAME", cast=str, default="postgres"),
        'USER': config("TEL_GAME_POSTDB_USER", cast=str, default="postgres"),
        'PASSWORD': config("TEL_GAME_POSTDB_PASSWORD", cast=str, default="postgres"),
        'HOST': config("POSTGRES_HOST", default="db", cast=str),
        'PORT': config("POSTDB_PORT", cast=int, default=5432),

        "OPTIONS": {
            "pool": True,
            # "min_size": config("POOL_MIN_SIZE", default=1, cast=int),
            # "max_size": config("POOL_MAX_SIZE", default=2, cast=int),
            # "timeout": 15,
        }
    }
}

CORS_ALLOWED_ORIGINS = "".join(config("PROD_CORS_ORIGIN", cast=list)).split(",")



# with logging django
log_dir = os.path.join(BASE_DIR / "general_log_django", timezone.now().strftime("%Y-%m-%d"))
os.makedirs(log_dir, exist_ok=True)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "color": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(levelname)s %(reset)s%(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "color",
            "filename": os.path.join(BASE_DIR / log_dir / "error_file.log")
        },
        "warning_file": {
            "level": "WARN",
            "class": "logging.FileHandler",
            "formatter": "color",
            "filename": os.path.join(BASE_DIR / log_dir / "warning_file.log")
        },
        "critical_file": {
            "level": "CRITICAL",
            "class": "logging.FileHandler",
            "formatter": "color",
            "filename": os.path.join(BASE_DIR / log_dir / "critical_file.log")
        },
    },
    "loggers": {
        "django": {
            "handlers": [ "warning_file", "critical_file", "error_file"],
            "propagate": True,
        }
    }
}