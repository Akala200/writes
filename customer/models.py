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
    balance = models.DecimalField(decimal_places=2, max_digits=1000)






