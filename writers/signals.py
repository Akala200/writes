from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from .models import WritersProfile



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_writers(sender, created, instance, **kwargs):
    if created and instance.is_writer:
        profile = WritersProfile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_user(sender, created, instance, **kwargs):
    if created:
        instance.is_writer = True
        instance.save()
    


