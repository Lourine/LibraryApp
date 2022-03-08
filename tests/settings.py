import os
import dj_database_url
from LibraryApp.config.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS.remove('django_extensions')

# # Application definition

# INSTALLED_APPS += []

ROOT_URLCONF = 'LibraryApp.config.urls'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lib',
        'USER': 'wangari',
        'PASSWORD': '7890',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# if os.environ.get('GITHUB_WORKFLOW'):
#     DATABASES = {
#         'default': {
#            'ENGINE': 'django.db.backends.postgresql',
#            'NAME': 'postgres',
#            'USER': 'app',
#            'PASSWORD': 'app',
#            'HOST': '127.0.0.1',
#            'PORT': '5432',
#         }
#     }
