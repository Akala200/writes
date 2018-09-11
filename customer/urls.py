from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('process-payment/', views.process_payment, name='process-payment'),
    path('payment-form/', views.payment_button, name='payment-form'),
    path('charge-payment/', views.charge_payment, name='charge-payment'),
    path('payment-completed/', views.payment_completed, name='payment_completed')
]
