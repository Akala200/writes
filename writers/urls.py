from django.urls import path

from . import views

app_name = 'writers'

urlpatterns = [
    path('signup/', views.signup, name='writer-signup'),
    path('home/', views.Home.as_view(), name='home'),
    path('all_bids/', views.AllBids.as_view(), name='all_orders'),
    #path('bidding/', views.all_orders, name='bidding'),
    path('bid-progress/', views.in_progress, name='in_progress'),
    #path('new-orders/', views.new_orders, name='new_orders'),
    path('personal/', views.personal, name='personal'),
    path('create-profile/', views.create_profile, name='create-profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('user-detail/<str:writer_name>/', views.writer_profile_detail, name='writer_profile_detail'),
    path('view-transaction/', views.view_transactions, name='view_transactions'),
    path('new-orders/', views.NewOrders.as_view(), name='new_order'),
    path('active-bid/', views.BidsProgress.as_view(), name='active_bid'),
    path('order-details/<int:order_uuid>/', views.order_details, name='order_detail'),
    path('place-a-bid/<int:order_uuid>/', views.place_a_bid, name='place_a_bid'),
    path('completed-bid/', views.CompletedOrders.as_view(), name='completed_bid'),
    path('expired-bid/', views.ExpiredOrders.as_view(), name='expired_bid'),
    path('view-bid-inprogress/<int:pk>/', views.BidInProgressDetaill.as_view(), name='inprogress'),
    path('upload-file/<int:bid_id>/', views.upload_assignment_file, name='upload_assignment_file'),
    path('view-assignment/<int:pk>/', views.ViewAssignment.as_view(), name='view_assignment'),
    path('delete-file/<int:file_id>/', views.delete_uploaded_file, name='delete_uploaded_file')


]