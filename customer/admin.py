from django.contrib import admin

# Register your models here.

from .models import WalletBalance, Wallet, Order,  Hired, FavouriteWriters, AdditionalFiles, Offers
from writers.models import Bids


admin.site.register(WalletBalance)
admin.site.register(Order)
admin.site.register(FavouriteWriters)
admin.site.register(Bids)
admin.site.register(Offers)

admin.site.register(Wallet)
admin.site.register(AdditionalFiles)
admin.site.register(Hired)