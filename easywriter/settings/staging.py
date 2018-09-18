from .base import *


from decouple import config

STATICFILES_DIRS = ( os.path.join('static'), )


STATICFILES_DIRS = ( os.path.join('static'), )




DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
       'NAME': 'sqlite3.db', 
       'HOST': '127.0.0.1',
       'PORT': ''
   }
    

}

