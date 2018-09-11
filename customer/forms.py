from django import forms

from .models import Wallet


class PaymentForm(forms.Form):
    amount = forms.CharField(max_length=20)



