"""
Django settings for mongo_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    ('{{ cookiecutter.admin_login }}', '{{ cookiecutter.e_mail }}'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE_ME'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'djangotoolbox',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ cookiecutter.nome_do_projeto }}.urls'

WSGI_APPLICATION = '{{ cookiecutter.nome_do_projeto }}.wsgi.application'

{ % if cookiecutter.cloudfoundry == "y" %}
# Database
# https://django-mongodb-engine.readthedocs.io/en/latest/index.html

if DEBUG:
    #################################################
    # Local mongodb database
    #################################################
    DATABASES = {
        'default': {
            'ENGINE': 'django_mongodb_engine',
            'NAME': '{{ cookiecutter.local_mongo_database_name }}',
        }
    }

else:
    #################################################
    # mlab mongodb database
    #################################################
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    uri = unicode(vcap_services['mlab'][0]['credentials']['uri'])

    g = re.match('^mongodb\://(.*):(.*)@(.*):([0-9]*)\/(.*)$', uri)

    mongo_connect = {
        "username": g.group(1),
        "password": g.group(2),
        "hostname": g.group(3),
        "port": g.group(4),
        "db_name": g.group(5),
    }

    DATABASES = {
        'default': {
            'ENGINE': 'django_mongodb_engine',
            'NAME': mongo_connect['db_name'],
            'USER': mongo_connect['username'],
            'PASSWORD': mongo_connect['password'],
            'HOST': mongo_connect['hostname'],
            'PORT': mongo_connect['port'],
        }
    }

{ % else %}
# Database
# https://django-mongodb-engine.readthedocs.io/en/latest/index.html

# Descomente para o deploy
#################################################
# mlab mongodb database
#################################################
# vcap_services = json.loads(os.environ['VCAP_SERVICES'])
# uri = vcap_services['mlab'][0]['credentials']
#
# g = re.match('^mongodb\://(.*):(.*)@(.*):([0-9]*)\/(.*)$', uri)
#
# mongo_connect = {
#     "username": g.group(1),
#     "password": g.group(2),
#     "hostname": g.group(3),
#     "port": g.group(4)),
#     "db_name": g.group(5),
# }
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_mongodb_engine',
#         'NAME': mongo_connect['db_name'],
#         'USER': mongo_connect['username'],
#         'PASSWORD': mongo_connect['password'],
#         'HOST': mongo_connect['hostname'],
#         'PORT': mongo_connect['port'],
#     }
# }

#################################################
# Local mongodb database
#################################################
DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': '{{ cookiecutter.local_mongo_database_name }}',
    }
}
{ % endif %}


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
