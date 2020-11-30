"""
Django settings for quantum_common project.

Generated by 'django-admin startproject' using Django 2.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    CONSOLE_LOG_FORMAT=(
        str,
        '%(levelname)s %(asctime)s %(process)d:%(threadName)s %(name)s %(module)s:%(funcName)s:%(lineno)d %(message)s'
    ),
    ALLOWED_HOSTS=(list, ['*']),
    ENVIRONMENT_NAME=(str, '__dev__'),
    VERBOSE_LOGGING=(bool, False),
    VERBOSE_LOGGING_TEMPLATE=(bool, False),
    VERBOSE_LOGGING_SQL=(bool, False),
    ENABLE_DJANGO_EXTENSIONS=(bool, False),
    MEDIA_ROOT=(str, os.path.join(BASE_DIR, 'media')),
    STATIC_ROOT=(str, os.path.join(BASE_DIR, 'collectedstatic')),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'data',
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

ROOT_URLCONF = 'quantum_common.urls'

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
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quantum_common.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = env('STATIC_ROOT')
STATIC_URL = '/static/'
MEDIA_ROOT = env('MEDIA_ROOT')
MEDIA_URL = '/media/'

VERBOSE_LOGGING = env('VERBOSE_LOGGING')
VERBOSE_LOGGING_TEMPLATE = env('VERBOSE_LOGGING_TEMPLATE')
VERBOSE_LOGGING_SQL = env('VERBOSE_LOGGING_SQL')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG' if VERBOSE_LOGGING else 'INFO',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format':
            '%(levelname)s [%(asctime)s] %(process)d:%(threadName)s %(name)s %(module)s:%(funcName)s:%(lineno)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG' if VERBOSE_LOGGING else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.template': {
            'level': 'DEBUG' if VERBOSE_LOGGING_TEMPLATE else 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.utils.autoreload': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.db': {
            'level': 'DEBUG' if VERBOSE_LOGGING_SQL else 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        **{
            app.split('.')[0]: {
                'level': 'DEBUG' if VERBOSE_LOGGING else 'INFO',
                'handlers': ['console'],
                'propagate': False,
            }
            for app in INSTALLED_APPS + ['sentry_sdk', 'gunicorn.errors']
        }
    }
}
