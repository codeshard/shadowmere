import environ
from pathlib import Path
from datetime import date

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from celery.schedules import crontab
from django.utils.translation import gettext_lazy as _

env = environ.Env(
    DEBUG=(bool, False),
    SHADOWTEST_URL=(str, "https://shadowtest.akiel.dev/v1/test"),
    ALLOWED_HOSTS=(str, ""),
    CSRF_TRUSTED_ORIGINS=(str, ""),
    CORS_ALLOWED_ORIGINS=(str, ""),
    MINIO_ENDPOINT=(str, ""),
    MINIO_ACCESS_KEY=(str, ""),
    MINIO_SECRET_KEY=(str, ""),
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

SHADOWTEST_URL = env("SHADOWTEST_URL")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS: str = env("CSRF_TRUSTED_ORIGINS").split(" ")

CORS_ALLOWED_ORIGINS: str = env("CORS_ALLOWED_ORIGINS").split(" ")

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "storages",
    "import_export",
    "django_prometheus",
    "rangefilter",
    "rest_framework",
    "django_filters",
]

LOCAL_APPS = [
    "proxylist.apps.ProxylistConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "shadowmere.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shadowmere.wsgi.application"

DATABASES = {"default": env.db()}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(server_time)s] %(message)s",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        # Custom handler which we will use with logger 'django'.
        # We want errors/warnings to be logged when DEBUG=False
        "console_on_not_debug": {
            "level": "WARNING",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "console_on_not_debug"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ("es", _("Spanish")),
    ("en", _("English")),
]

LOCALE_PATHS = ("./locale",)

STATIC_URL = "/static/"

STATIC_ROOT = "./static_files/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BROKER_URL = "redis://redis:6379"

CELERY_RESULT_BACKEND = "redis://redis:6379"

CELERY_BEAT_SCHEDULE = {
    "update_status": {
        "task": "proxylist.tasks.update_status",
        "schedule": crontab(minute="*/20"),
    },
    "poll_subscriptions": {
        "task": "proxylist.tasks.poll_subscriptions",
        "schedule": crontab(hour="*/6"),
    },
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "proxylist.pagination.ProxiesPagination",
    "PAGE_SIZE": 10,
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

CONN_MAX_AGE = 60

CONN_HEALTH_CHECKS = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HOSTS_INCLUDE_SUBDOMAINS = True

X_FRAME_OPTIONS = "SAMEORIGIN"

FILTERS_DEFAULT_LOOKUP_EXPR = "icontains"

JAZZMIN_SETTINGS = {
    "site_title": "Shadowmere Administration",
    "site_header": "Shadowmere",
    "site_brand": "Shadowmere",
    "welcome_sign": "Welcome to Shadowmere Administration",
    "copyright": f"Shadowmere {date.year}",
}
