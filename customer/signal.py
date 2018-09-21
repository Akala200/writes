from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Q

from pusher import Pusher

from .models import WalletBalance, Order
from writers.models import WritersProfile




pusher = Pusher(
    app_id="603993",
    key="39af9ceb44877b8cdef1",
    secret="fe402a157039ae2a42e4",
    cluster="eu")



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_portfolio_for_new_user(sender, created, instance, **kwargs):
    if created:
        wallet = WalletBalance.objects.create(balance_id=instance)


@receiver(post_save, sender=Order)
def live_dashboard_update(sender, created, instance, **kwargs):
    if created:
        search_writers = WritersProfile.objects.filter(Q(is_approved=True))
        if search_writers:
            pusher.trigger(u'order', u'send', {
                u'order_id': instance.order_uuid,
                u'topic': instance.topic,
                u'deadline': instance.deadline
            }
            )
            return 'Done'
        else:
            return "Not Done"
      
    



