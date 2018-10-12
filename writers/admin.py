from django.contrib import admin

# Register your models here.
from  .models import Rating, WritersProfile, InvitedWriters

admin.site.register(Rating)
admin.site.register(WritersProfile)
admin.site.register(InvitedWriters)
