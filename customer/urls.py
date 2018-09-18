from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('view-transactions/', views.view_transactions, name='view_transactions'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('home/', views.Index.as_view(), name='index'),
    path('cancelled-orders/', views.cancelled_order, name='cancelled_order'),
    path('completed-orders/', views.completed_order, name='completed_order'),
    path('bidding-orders/', views.bidding_order, name='bidding_order'),
    path('expired-orders/', views.expired_order, name='expired_order'),
    path('place-an-order/', views.place_an_order, name='place_an_order'),
    path('order-detail/<int:order_uuid>/', views.order_details, name='order_detail'),
    path('edit/<int:order_uuid>/', views.update_order, name='update_order'),
    path('declined/', views.declined_bids, name='declined'),
    path('hired/', views.hired_before, name='hired_before'),
    path('invited-writes/', views.invited_writers, name='invited_writers'),
    path('invited/', views.invited, name='invited'),
    path('new-bids/', views.new_bids, name='new_bids'),
    path('shortlisted/', views.shortlisted, name='short_listed'),
    path('view-all-bids/', views.view_all_bids, name='view_all_bigs'),
    path('additional-files/', views.additional_files, name='additional_files'),
    path('assign-writers', views.assign_writers, name='assign_writers'),
    path('<int:order_uuid>/add-files/', views.additional_files, name='additional_files'),
    path('<view./', views.view_favorite_writers, name='favorite_writers'),
    path('cancel-order/<int:order_uuid>/', views.cancel_an_order, name='cancel_an_order'),
    path('resubmit-order/<int:order_uuid>/', views.resubmit_order, name='resubmit_order')

]
