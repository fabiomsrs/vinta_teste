# https://docs.djangoproject.com/en/1.10/ref/settings/

import os

from decouple import config  # noqa


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


SITE_ID = 1

SECURE_HSTS_PRELOAD = True

DEBUG = True

ADMINS = (("Admin", "fabiomsrs@gmail.com"),)

AUTH_USER_MODEL = "users.User"

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [         
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_js_reverse",
    "webpack_loader",
    "django_filters",
    "rest_framework",
    "import_export",
    'social_django',
    "common",
    "users",
    "core",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = "vinta_teste.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [base_dir_join("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "common.context_processors.sentry_dsn",
                "common.context_processors.commit_sha",
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = "vinta_teste.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

CORS_ORIGIN_ALLOW_ALL = True

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (base_dir_join("../frontend"),)

# Webpack
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": False,  # on DEBUG should be False
        "STATS_FILE": base_dir_join("../webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "IGNORE": [".+\.hot-update.js", ".+\.map"],
    }
}

# Celery
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACKS_LATE = True
CELERY_TIMEZONE = TIME_ZONE

# Sentry
SENTRY_DSN = config("SENTRY_DSN", default="")
COMMIT_SHA = config("HEROKU_SLUG_COMMIT", default="")

LOGIN_URL = 'users:login'
LOGOUT_URL = 'users:logout'
LOGIN_REDIRECT_URL = 'users:login'
LOGOUT_REDIRECT_URL = 'users:login'

SOCIAL_AUTH_GITHUB_KEY = '697942c37b2a45efe29b'
SOCIAL_AUTH_GITHUB_SECRET = '7401518acd664aafb4d1ded8be0d6ce838bb185f'

SOCIAL_AUTH_GITHUB_SCOPE = [
    'user:email', 'repo', 'admin:repo_hook'
]

SOCIAL_AUTH_STORAGE = 'users.storage.DjangoSocial'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DATETIME_FORMAT': "%d/%m/%Y %H:%M:%S",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
