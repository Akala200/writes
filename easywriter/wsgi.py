import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easywriter.settings.staging")

application = get_wsgi_application()
