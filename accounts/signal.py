from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_portfolio_for_new_user(sender, created, instance, **kwargs):
    if created:
        instance.is_user = True
        instance.save()

@receiver(user_logged_in)
def user_online_status(request, user, **kwargs):
    user.login_status = True
    user.save()    


@receiver(user_logged_out)
def user_offline_status(request, user, **kwargs):
    if user:
        user.login_status = False
        user.save()   

