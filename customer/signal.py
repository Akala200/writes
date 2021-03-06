import json

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder

from pusher import Pusher

from .models import WalletBalance, Order, Offers
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

"""
@receiver(post_save, sender=Order)
def live_dashboard_update(sender, created, instance, **kwargs):
    if created:
        #search_writers = WritersProfile.objects.filter(Q(is_approved=True))
        date = json.dumps(instance.deadline, cls=DjangoJSONEncoder)
        print(date)
        pusher.trigger('Aeronautics', u'add', {
            u'order_id': instance.order_uuid,
            u'topic': instance.topic,
            u'deadline': date
            })
        print('DOne')
        return 'Done'
    else:
        return "Not Done"
"""   

@receiver(post_save, sender=Order)
def create_oofers(sender, created, instance, **kwargs):
    if created:
        Offers.objects.create(offer_id=instance)




