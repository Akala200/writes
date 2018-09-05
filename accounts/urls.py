from django.urls import path, include

from  . import views


urlpatterns = [
    path('login/', views.Login.as_view(), name='account_login' ),
    path('' , include('allauth.urls'))
]