from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-6v4_^n8eqth0wtm*573jwqn*bjn=)xd9h(cetgqcq$vq1d14y9"

DEBUG = True
SESSION_COOKIE_AGE = 3600

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["https://test.oildrive.uz", "https://oildrive.uz", "https://oildrive.pythonanywhere.com"]


INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    'django.contrib.sites',
    "ckeditor",
    'treebeard',
    "main_page",
    "modeltranslation",
    "cms",
    "menus",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "oil_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "oil_web.wsgi.application"


# if DEBUG:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': 'postgres',
#             'USER': 'postgres',
#             'PASSWORD': 'postgres',
#             'HOST': 'db',
#             'PORT': 5432
#         }
#     }


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


LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "assets")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_UPLOAD_PATH = "uploads/"  # Путь для загружаемых файлов
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",  # Уровень инструментов
        "height": 300,  # Высота редактора
        "width": 800,  # Ширина редактора
    },
}

LANGUAGES = [
    ("uz", "Uzbek"),
    ("ru", "Russian"),
    ("en", "English"),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

USE_L10N = True

# MODELTRANSLATION_FALLBACK_LANGUAGES = {
#     'default': ('original',),  # Использование оригинального поля, если перевод отсутствует
# }
