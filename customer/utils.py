from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


def invite_writer(recipent, **context):
    invite = render_to_string('user/invite_writers.html', context=context)
    return send_mail(subject='Invitation to place a bid for an Order', message=invite, 
    from_email=settings.EMAIL_HOST_USER, recipient_list=[recipent])