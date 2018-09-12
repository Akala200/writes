from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_portfolio_for_new_user(sender, created, instance, **kwargs):
    if created:
        instance.is_user = True
        instance.save()
    

