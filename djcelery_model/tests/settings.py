# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import os

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery_model',
    'djcelery_model.tests.testapp',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates'),
        ],
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

ROOT_DIR = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(ROOT_DIR, 'test-static')
MEDIA_ROOT = os.path.join(ROOT_DIR, 'test-media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', POSTGRES_USER),
        'USER': POSTGRES_USER,
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_5432_TCP_PORT', '5432'),
    }
}

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_6379_TCP_PORT', '6379')
REDIS_LOCATION = '%s:%s' % (REDIS_HOST, REDIS_PORT)
CELERY_BROKER_URL = 'redis://%s/0' % REDIS_LOCATION
CELERY_RESULT_BACKEND = 'redis://%s/2' % REDIS_LOCATION
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_SEND_SENT_EVENT = True
CELERY_SEND_EVENTS = True
