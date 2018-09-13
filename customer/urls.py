from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('view-transactions/', views.view_transactions, name='view_transactions'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-form/', views.payment_button, name='payment_form'),
    path('charge-payment/', views.charge_payment, name='charge_payment'),
    path('home/', views.index, name='index'),
    path('cancelled-orders/', views.cancelled_order, name='cancelled_order'),
    path('completed-orders/', views.completed_order, name='completed_order'),
    path('bidding-orders/', views.bidding_order, name='bidding_order'),
    path('expired-orders/', views.expired_order, name='expired_order'),
    path('place-an-order/', views.place_an_order, name='place_an_order')
]
