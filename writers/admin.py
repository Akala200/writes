from django.contrib import admin

# Register your models here.
from  .models import Rating, WritersProfile

admin.site.register(Rating)
admin.site.register(WritersProfile)