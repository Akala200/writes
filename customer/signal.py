from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from .models import WalletBalance



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_portfolio_for_new_user(sender, created, instance, **kwargs):
    if created:
        wallet = WalletBalance.objects.create(user=instance)
    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.wallet_balance.save()