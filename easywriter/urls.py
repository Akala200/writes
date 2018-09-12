
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('global.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('au/', include('australia.url(s', namespace='au')),
    path('ca/', include('canada.urls', namespace='ca')),
    path('uk/', include('united_kingdom.urls', namespace='uk')),
    path('uae/', include('uae.urls', namespace='uae')),
    path('blog/', include('blog.urls')),
    path('customer/', include('customer.urls', namespace='customer'))
]

