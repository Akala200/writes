from django.contrib import admin

# Register your models here.

from .models import WalletBalance, Wallet


admin.site.register(WalletBalance)
admin.site.register(Wallet)