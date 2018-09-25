from django.conf import settings
from templated_email import send_templated_mail

def invite_writer(recipent, **context):
    invite = send_templated_mail(template_name='invite_writer', from_email=settings.EMAIL_HOST_USER,
    recipient_list=[recipent], context=context)
    return invite