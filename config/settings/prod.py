from .base import *
from decouple import config

DEBUG = False

# Allow Railway domain (temporary wildcard)
ALLOWED_HOSTS = ["*"]

# Static files
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False
# SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)


# Logging (important for debugging in Railway logs)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}