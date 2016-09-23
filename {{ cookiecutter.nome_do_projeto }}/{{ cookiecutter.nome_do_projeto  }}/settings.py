"""
Django settings for mongo_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cck#4hiycu!@w)69!rq)vdewlu)2r=$x)m@3jnwqi%p$38-eau'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import logging

if DEBUG:
    # will output to your console
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
    )
else:
    # will output to logging file
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
        filename = '/logs_django.log',
        filemode = 'a'
    )

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

USE_X_FORWARDED_HOST = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'djangotoolbox',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'project_teste',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mongo_django.urls'

WSGI_APPLICATION = 'mongo_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
import json
import re

# TODO: Consertar este trecho aqui abaixo, pois funciona com o mongodb
# vcap_services = json.loads(os.environ['VCAP_SERVICES'])
# uri = vcap_services['mlab'][0]['credentials']
#
# g = re.match('^mongodb\://(.*):(.*)@(.*):([0-9]*)\/(.*)$', uri)
#
# mongo_connect = {
#         "username": g.group(1),
#         "password": g.group(2),
#         "hostname": g.group(3),
#         "port": int(g.group(4)),
#         "db_name": g.group(5),
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': u'CloudFoundry_3kg6rngl_j1pqigc9', #mongo_connect['db_name'],
        'USER': u'CloudFoundry_3kg6rngl_j1pqigc9_s3qoenrp', #mongo_connect['username'],
        'PASSWORD': u'A1JcccKvPIc2ZtWNC_ne-JESe57nLSs2', #mongo_connect['password'],
        'HOST': u'ds035776.mlab.com', #mongo_connect['hostname'],
        'PORT': u'35776', #mongo_connect['port'],
        # 'OPTIONS': {
        #     'uri': db_credentials['uri'],
        # }
    }
}

# DATABASES = {
#    'default' : {
#       'ENGINE' : 'django_mongodb_engine',
#       'NAME' : 'banco_teste'
#    }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# whitenoise config
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
