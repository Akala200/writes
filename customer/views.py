from decimal import Decimal

from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.db.models import F
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from .forms import PaymentForm
from .models import Wallet, WalletBalance

import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required()
def process_payment(request):
    form = PaymentForm(request.POST)
    if request.method == "POST" and form.is_valid():
        request.session['amount'] = form.cleaned_data['amount']
        return redirect(reverse('customer:payment-form'))
  
    else:
        return render(request, 'customer/make_payment.html', context={'form': form})
        
@login_required()
def payment_button(request):
    if 'amount' in request.session:
        stripe_key = settings.STRIPE_PUBLIC_KEY
        amount = request.session['amount']
        request.session['payment_process'] = True
        return render(request, 'customer/process_payment.html', context={
            'stripe_key': stripe_key,
            'amount': amount})
    
    return HttpResponseBadRequest('invalid request')

@login_required()
def charge_payment(request):
    if request.method == 'POST' and 'payment_process' in request.session:
        amount = request.session.get('amount')
        token = request.POST.get('stripeToken')
        description = 'Payed with Card'
        try:
            charge = stripe.Charge.create(
                amount = amount,
                currency = 'usd',
                description = description,
                source = token
            )
        except stripe.error.CardError:
            return render(request, 'customer/card_error.html')
        
        except stripe.error.AuthenticationError:
            return render(request, 'customer/auth_error.html')

        except stripe.error.InvalidRequestError:
            return render(request, 'customer/error.html')

        else:
            payment_data = Wallet.objects.create(
                wallet_id = request.user,
                credit = amount,
                description = description,
                status = True
    
            )
            update_user_balance = WalletBalance.objects.get(balance_id=request.user)
            update_user_balance.balance += Decimal(amount)
            update_user_balance.save()
            request.session['payment_completed'] = True
            del request.session['amount']
            del request.session['payment_process']
            
            return redirect(reverse('customer:payment_completed'))
    return HttpResponseBadRequest('something happened')


@login_required()
def payment_completed(request):
    if 'payment_completed' not in request.session:
        return HttpResponseBadRequest('invalid request' )
    else:
        return render(request, 'payment_confirmation.html')








