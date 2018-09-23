from django.contrib import admin

# Register your models here.

from .models import WalletBalance, Wallet, Order,  FavouriteWriters, ShortListed, AdditionalFiles
from writers.models import Bids


admin.site.register(WalletBalance)
admin.site.register(Order)
admin.site.register(FavouriteWriters)
admin.site.register(Bids)
admin.site.register(ShortListed)
admin.site.register(Wallet)
admin.site.register(AdditionalFiles)