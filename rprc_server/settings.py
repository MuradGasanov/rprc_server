# -*- coding: utf-8 -*-

import os
import socket

if socket.gethostname() in ("Admin-PC",):
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
PROJECT_PARENT_PATH = os.path.dirname(PROJECT_PATH)


def path(p):
    return p.replace('\\', '/')


ADMINS = (
    ('Murad Gasanov', 'gmn1791@ya.ru'),
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rprc',
        'USER': 'rprc',
        'PASSWORD': 'rprc',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = path(os.path.join(PROJECT_PARENT_PATH, "rprc_static/media"))

MEDIA_URL = '/media/'

STATIC_ROOT = path(os.path.join(PROJECT_PARENT_PATH, "rprc_static/static"))

STATIC_URL = '/static/'

STATICFILES_DIRS = ("static",
   #  path(os.path.join(PROJECT_PATH, "static")),
)

LOGIN_URL = "/login"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'd*_9*!x5@hy7t!uw&zv2n!nu=((#g97-arqhn=i5hjs@5pxi-f'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.templates.loaders.eggs.Loader',
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'main.auth_backends.CustomUserModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)

CUSTOM_USER_MODEL = 'main.Controller'

ROOT_URLCONF = 'rprc_server.urls'

WSGI_APPLICATION = 'rprc_server.wsgi.application'

TEMPLATE_DIRS = ('templates',)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}