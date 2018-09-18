from .base import *


from decouple import config


STATICFILES_DIRS = (os.path.join('static'),)


DATABASES = {
   'default': {
       'ENGINE':'django.db.backends.postgresql',
       'NAME': config('DB_NAME'),
       'USER': config('DB_USER'),
       'PASSWORD': config('DB_PASSWORD'),
       'HOST': '127.0.0.1',
       'PORT': ''
   }
    

}

