from .base import *


from decouple import config


STATICFILES_DIRS = (os.path.join('static'),)


DATABASES = {
   'default': {
       'ENGINE':'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'sqlite3'),
       #'USER': config('DB_USER'),
       #'PASSWORD': config('DB_PASSWORD'),
       #'HOST': '127.0.0.1',
       #'PORT': ''
   }


}

