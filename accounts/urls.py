from django.urls import path, include

from  . import views


urlpatterns = [
    path('' , include('allauth.urls')),
    path('login', views.LoginUserView.as_view(), name='logged_in_users')
]