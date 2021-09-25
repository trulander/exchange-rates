"""
Django settings for exchangerates project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def get_env(variable_name, default=None):
    value = os.getenv(variable_name)

    if value is None:
        if default is not None:
            return default
        raise ValueError(f"{variable_name} is not presented in environment variables. Check your .env file")
    if str(value).lower() in ("true", "false"):
        return str(value).lower() == "true"
    return value

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rh_9bwu3q1ked##=l5!6wzqv=$m&^qb_oic7eqg))8lh%f12yk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env('DEBUG')

ALLOWED_HOSTS = get_env('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'django_celery_beat',
    'django_celery_results',

    'Core.Models',
    'services',
    'api',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exchangerates.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'exchangerates.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if get_env('DATABASE_TYPE') == 'sqlite' else {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env("DATABASE_NAME"),
        "USER": get_env("DATABASE_USER"),
        "PASSWORD": get_env("DATABASE_PASSWORD"),
        "HOST": get_env("DATABASE_HOST"),
        "PORT": "5432",
        "CONN_MAX_AGE": None
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# RestFramework
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES':[
    #     'rest_framework.permissions.IsAdminUser',
    # ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':10
}


# Celery Configuration Options
CELERY_CONFIGURATION = {
    "broker_url": f"{get_env('CELERY_BROKER_URL')}/1",
    "result_backend": f"{get_env('CELERY_RESULT_BACKEND')}",
    "celery_timezone": "Europe/Moscow",

    "beat_schedule": {
        "update rate": {
            "task": "services.tasks.update_exchange",
            "schedule": int(get_env('MAIN_TASK_CELERY_SHEDULE')),
            "kwargs": {"id": int(get_env('MAIN_TASK_CELERY_CURRENCY_ID'))}
        },
    },
    "beat_scheduler": "django_celery_beat.schedulers:DatabaseScheduler",
    "beat_sync_every": 1
}


# service coinmarketcap.com
URL_API_GET_ACTUALL_CURRENCY = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
API_KEY = {'CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd'}