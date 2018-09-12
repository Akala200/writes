from decimal import Decimal

from django.db import models
from django.conf import settings

class Wallet(models.Model):
    wallet_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    credit = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.wallet_id)


class WalletBalance(models.Model):
    balance_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    related_name='wallet_balance'
    )
    balance = models.DecimalField(decimal_places=2, max_digits=1000, default=Decimal('0.00'))

    def __str__(self):
        return str(self.balance_id)


class Order(models.Model):
    order_choice = (
        ('')
    )

    page_choice = (
        ('1 pages/275 words', '1 pages/275 words'),
        ('2 pages/550 words', '2 pages/550 words'),
        ('3 pages/825 words', '3 pages/825 words'),
        ('4 pages/1100 words', '4 pages/1100 words'),
        ('5 pages/1375 words', '5 pages/1375 words'),
        ('6 pages/1650 words', '6 pages/1650 words'),
        ('7 pages/1925 words', '7 pages/1925 words'),
        ('8 pages/2200 words', '8 pages/2200 words'),
        ('9 pages/2475 words', '9 pages/2475 words'),
        ('10 pages/2750 words', '10 pages/2750 words'),
        ('11 pages/3025 words', '11 pages/3025 words'),
        ('12 pages/3300 words', '12 pages/3300 words'),
        ('13 pages/3575 words', '13 pages/3575 words'),
        ('14 pages/3850 words', '14 pages/3850 words'),
        ('15 pages/4125 words', '15 pages/4125 words'),
        ('16 pages/4400 words', '16 pages/4400 words'),
        ('17 pages/4675 words', '17 pages/4675 words'),
        ('18 pages/4950 words', '18 pages/4950 words'),
        ('19 pages/5225 words', '19 pages/5225 words')

    )
    
    service_choice = (
        ('Writing', 'Writing'),
        ('Editing', 'Editing'),
        ('Rewriting', 'Rewriting')

    )

    source_choice = (
        ('0 source','0 source'),
        ('1 source', '1 source'),
        ('2 source', '2 source'),
        ('3 source', '3 source'),
        ('4 source', '4 source'),
        ('5 source', '5 source'),
        ('7 source', '7 source')

    )

    style_choice = (

    )

    subject_choice = (

    )

    level_choice = (
        ('School', 'School'),
        ('University', 'University'),
        ('Dictorate', 'Dictorate'),


    )

    order_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.CharField(max_length=250)
    description = models.TextField()
    order_uuid = models.IntegerField(unique=True)
    order_type = models.CharField(max_length=250)
    pages  = models.CharField(max_length=250)
    service =  models.CharField(max_length=250)
    deadline = models.DateTimeField()
    sources = models.CharField(max_length=250)
    style  = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.order_id)


class FavouriteWriters(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    writers = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return str(self.user)


class InvitedWriters(models.Model):
    user = models.ForeignKey(Order, on_delete=models.CASCADE)
    invitees = models.CharField(max_length=250, null=True)


class AdditionalFiles(models.Model):
    user = models.ForeignKey(Order, on_delete=models.CASCADE)
    files = models.FileField(upload_to='addtion_files')
    
    
    def __str__(self):
        return str(self.user)





