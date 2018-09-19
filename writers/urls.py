from django.urls import path

from . import views

app_name = 'writers'

urlpatterns = [
    path('signup/', views.signup, name='writer-signup'),
    path('home/', views.home, name='home'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('bidding/', views.all_orders, name='bidding'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('bid-progress/', views.in_progress, name='in_progress'),
    path('new-orders/', views.new_orders, name='new_orders'),
    path('personal/', views.personal, name='personal'),
    path('create-profile/', views.create_profile, name='create-profile')


]