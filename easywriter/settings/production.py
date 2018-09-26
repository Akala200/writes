
from .base import *

import dj_database_url
from decouple import config


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(DIR, 'static')

SECURE_SSL_REDIRECT = True



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')



DATABASES = {}

DATABASES['default'] =  dj_database_url.config(default=config('DATABASE_URL'))
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'