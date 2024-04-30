from .common import *
import dj_database_url
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')

DATABASES =  {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'