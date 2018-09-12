from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('view-transactions/', views.view_transactions, name='view_transactions'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-form/', views.payment_button, name='payment_form'),
    path('charge-payment/', views.charge_payment, name='charge_payment'),
    path('home', views.index, name='index')
]
