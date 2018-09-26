
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('global.urls')),
    path('admin/', admin.site.urls),
    path('writer/', include('writers.urls', namespace='writers')),
    path('accounts/', include('accounts.urls')),
    path('au/', include('australia.urls', namespace='au')),
    path('ca/', include('canada.urls', namespace='ca')),
    path('uk/', include('united_kingdom.urls', namespace='uk')),
    path('uae/', include('uae.urls', namespace='uae')),
    path('blog/', include('blog.urls')),
    path('customer/', include('customer.urls', namespace='customer')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

