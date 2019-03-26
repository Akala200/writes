from django.urls import path, include

from . import views

app_name = 'customer'

urlpatterns = [
    path('view-transactions/', views.view_transactions, name='view_transactions'),
    path('execute-payment/', views.execute_payment, name='execute_payment'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('home/', views.Index.as_view(), name='index'),
    path('cancelled-orders/', views.cancelled_order, name='cancelled_order'),
    path('completed-orders/', views.completed_order, name='completed_order'),
    path('in_progress-orders/', views.order_in_progress, name='order_in_progress'),
    path('expired-orders/', views.expired_order, name='expired_order'),
    path('place-an-order/', views.place_an_order, name='place_an_order'),
    path('order-detail/<int:order_uuid>/', views.order_details, name='order_detail'),
    path('edit/<int:order_uuid>/', views.update_order, name='update_order'),
    path('declined/<int:order_uuid>/', views.DeclinedBids.as_view(), name='declined'),
    path('hired/<int:order_uuid>/', views.HiredBefored.as_view(), name='hired_before'),
    path('invite-writer/<int:order_uuid/<int:writer_id>', views.invite_writers, name='invite_writers'),
    path('invited/<int:order_uuid>/', views.Invited.as_view(), name='invited'),
    path('new-bids/', views.new_bids, name='new_bids'),
    path('shortlisted/<int:order_uuid>/', views.ShortListedList.as_view(), name='short_listed'),
    path('view-all-bids/', views.view_all_bids, name='view_all_bids'),
    path('additional-files/<int:order_uuid>/', views.additional_files, name='additional_files'),
    path('assign-writers/<int:order_uuid>/', views.AssignWriters.as_view(), name='assign_writers'),
    path('add-files/<int:order_uuid>/', views.add_additional_file, name='add_files'),
    path('view-favorite/', views.FavoriteWriter.as_view(), name='favorite_writers'),
    path('cancel-order/<int:order_uuid>/', views.cancel_an_order, name='cancel_an_order'),
    path('resubmit-order/<int:order_uuid>/', views.resubmit_order, name='resubmit_order'),
    path('view-writers/', views.ViewAllWriters.as_view(), name='view_all_writers'),
    path('remove-writer/<int:writer_id>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('add-favorite/<int:writer_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('favorite-writers/<int:order_uuid>/', views.FavoriteWriterBids.as_view(), name='favorites'),
    path('bidding-order/<int:order_uuid>/', views.bidding_order, name='bidding-order'),
    path('delete-file/<int:file_id>/', views.delete_uploaded_file, name='delete_file'),
    path('cancel-payment', views.cancel_payment, name='cancel_payment'),
    path('hired-writer/<int:order_uuid>/', views.hired_writer, name='hired_writer'),
    path('view-bid/<int:order_uuid>/', views.view_all_bids, name='view_bids'),
    path('view-assignment-files/<int:order_uuid>/<int:bid_id>/', views.download_assignment, name='download_assignment'),
    path('accept-bid', views.accept_bid_order, name='accept_bid_order' ),
    path('place-order-writer/<int:writer_id>/', views.place_order_for_a_writer, name='place_order_for_a_writer'),
    path('shortlist_a_bid/', views.shortlist_a_bid_ajax, name='shortlist_a_bid_ajax'),
    path('remove_from_shorlist/', views.remove_from_shortlist_ajax, name='remove_from_shortlist_ajax'),
    path('decline_a_bid/', views.decline_a_bid_ajax, name='decline_a_bid_ajax'),
    path('order_details/<int:order_uuid>/', views.order_details_ajax, name='order_details_ajax')

]
