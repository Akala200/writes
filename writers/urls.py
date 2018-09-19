from django.urls import path

from . import views

app_name = 'writers'

urlpatterns = [
    path('signup', views.signup, name='writer-signup')
]