from django import forms

from .models import Wallet


class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '$'
    }))



