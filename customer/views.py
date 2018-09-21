import random
import json
from decimal import Decimal

import stripe

from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from django.db.models import F, Q
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView

from .forms import PaymentForm, PlaceAnOrderForm, CancelOrderForm
from .models import (
    Wallet, WalletBalance, Order, FavouriteWriters,
    Hired, AdditionalFiles, ShortListed

)

from writers.models import Bids, WritersProfile

import django_tables2 as tables



stripe.api_key = settings.STRIPE_SECRET_KEY


def generated_unique_id():
    ran = ''.join(str(random.randint(2, 8)) for x in range(6))
    return ran


class OrderTable(tables.Table):
    class Meta:
        model = Order



class Index(LoginRequiredMixin, TemplateView, ListView):
    model = Order
    context_object_name = 'orders'

    template_name = 'users/user_oders.html'

    def get_queryset(self):
        queryset = Order.objects.filter(order_id=self.request.user).order_by('-deadline').all()
        return queryset


@login_required()
def bidding_order(request):
    return render(request, '')

@login_required()
def cancelled_order(request):
    cancelled = Order.objects.filter(Q(order_id=request.user), Q(cancelled=True))
    return render(request, 'customer/orders/canceled_orders.html', context={'orders':  cancelled }) 

@login_required()
def completed_order(request):
    return render(request, 'customer/orders/completed_orders.html')

@login_required()
def expired_order(request):
    return render(request, 'customer/orders/expired_order.html')

@login_required()
def place_an_order(request):
    form = PlaceAnOrderForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.order_id = request.user
            instance.order_uuid = generated_unique_id()
            instance.deadline = timezone.now()
            form.save()
            messages.success(request, 'Your Order was created successfully')
            return redirect(reverse('customer:index'))


        else:
            messages.error(request, 'Failed to create an order')
            form = PlaceAnOrderForm()

    return render(request, 'users/place_order.html', context={
        'form': form
    })

@login_required()
def cancel_an_order(request, order_uuid):
    form = CancelOrderForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        cancel_order = Order.objects.filter(order_uuid=order_uuid).update(cancelled=True)
        messages.success(request, 'Order cancelled successfully')
        return redirect(reverse('customer:index'))



@login_required()
def view_transactions(request):
    wallet = Wallet.objects.filter(wallet_id=request.user).order_by('-date')
    wallet_balance = WalletBalance.objects.get(balance_id=request.user)
    context = {'wallet': wallet, 'wallet_balance': wallet_balance}
    return render(request, 'customer/wallet/wallet.html', context=context)

@login_required()
def process_payment(request):
    stripe_key = settings.STRIPE_PUBLIC_KEY
    form = PaymentForm(request.POST)
    if request.method == "POST" and form.is_valid():
        amount = form.cleaned_data['amount']
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
            
            return render(request, 'customer/wallet/error.html')

        else:
            payment_data = Wallet.objects.create(
                wallet_id = request.user,
                credit = amount,
                description = description,
                status = True
    
            )
            update_user_balance = WalletBalance.objects.filter(balance_id=request.user).update(balance=F('balance') + Decimal(amount))

            
            return redirect(reverse('customer:view_transactions'))
            
    return render(request, 'customer/wallet/fund_wallet.html', context={'form': form,
    'stripe_key': stripe_key, 'amount': request.POST.get('amount')})
        


@login_required()
def order_details(request, order_uuid):
    order_id = get_object_or_404(Order, order_uuid=order_uuid)

    return render(request, 'customer/bids/assignment_details.html', context={
        'bid':  order_id
    })



@login_required()
def canceled_order(request, order_uuid):
    order = get_object_or_404(Order, order_uuid)
    order.cancelled = True
    order.save()
    messages.success(request, 'Order Cancelled ')
    return redirect(reverse('customer:index'))

@login_required()
def update_order(request, order_uuid):
    order = get_object_or_404(Order, order_uuid=order_uuid)
    form = PlaceAnOrderForm(request.POST, instance=order)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.order_id = request.user
            instance.save()
            messages.success(request, 'Order was Updated')
            return redirect(reverse('customer:order_detail', kwargs={'order_uuid': instance.order_uuid}))
        
    else:
        form = PlaceAnOrderForm(instance=order)


    return render(request, 'users/edit_order.html', context={
        'form': form, 'order': order
    })

@login_required()
def assign_writers(request):
    return render(request, 'customer/bids/assign_writer.html')


class DeclinedBids(LoginRequiredMixin, ListView):
    model = Bids
    context_object_name = 'bids'
    paginate_by = 10
    template_name = 'customer/bids/declined.html'
    """
    def get_queryset(self):
        queryset = self.model.objects.filter(Q(bidding_id=self.kwargs['order_uuid']), Q(declined=True))
        return queryset
    """


class ShortListedList(LoginRequiredMixin, ListView):
    model = ShortListed
    context_object_name = 'shortlist'
    paginate_by = 10
    template_name = 'customer/bids/shortlisted.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(short_id=self.kwargs['order_uuid']).all()
        return queryset

   

class CompletedBids(LoginRequiredMixin,  ListView):
    model = Bids
    context_object_name = 'bids'
    paginate_by = 10
    template_name = 'customer/bids/completed.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(Q(order_uuid=self.request.user), Q(completed=True))
        return queryset

@login_required()
def hired_before(request):
    return render(request, 'customer/bids/hired_before.html')


@login_required()
def invited_writers(request):
    return render(request, 'customer/bids/invite_writers.html')

class Invited(LoginRequiredMixin,  ListView):
    model = Order
    context_object_name = 'invite'
    paginate_by = 10
    template_name = 'customer/bids/invited.html'

    """
    def get_queryset(self):
        queryset = self.model.objects.filter(order_uuid=self.request.user).all()
        return queryset
    """



@login_required()
def new_bids(request):
    new_bids = Bids.objects.all().exclude(Q(approved=True), Q(shortlisted=True),
    Q(declined=True))
    return render(request, 'customer/bids/new_bids.html')




@login_required()
def view_all_bids(request):
    return render(request, 'customer/bids/view_all_bids.html')


@login_required
def additional_files(request, order_uuid):
    order_id = AdditionalFiles.objects.filter(user=order_uuid).all()
    return render(request, context={'order': order_id, 'order_id': order_uuid})


@login_required
def add_additional_file(request, order_uuid):
    form = AdditionalFileForm(request.POST)

    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.user = order_uuid
        instance.save()
        messages.success(request, 'File submitted sucessfully')
        return redirect(reverse(instance.get_absolute_url()))

    else:
        files = AdditionalFiles.objects.filter(user=order_uuid).all()
        return render(request, 'customer/bids/additonal_files.html')


class FavoriteWriter(LoginRequiredMixin,  ListView):
    template_name = 'users/writers/favorite.html'
    model = FavouriteWriters
    paginate_by = 10
    context_object_name = 'favorite'

    def get_queryset(self):
        queryset =  self.model.objects.filter(user=self.request.user).all()
        return queryset




@login_required()
def resubmit_order(request, order_uuid):
    order = get_object_or_404(Order, order_uuid=order_uuid)
    form = PlaceAnOrderForm(request.POST, instance=order)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.order_id = request.user
            instance.save()
            messages.success(request, 'Order submited')
            return redirect(reverse('customer:order_detail', kwargs={'order_uuid': instance.order_uuid}))
        
    else:
        form = PlaceAnOrderForm(instance=order)


    return render(request, 'customer/orders/edit_assignment.html', context={
        'form': form, 'order': order
    })


@login_required()
def add_to_favorite(request, writer_id):
    writer_check = get_user_model().objects.filter(pk=writer_id)
    add_writer = FavouriteWriters.objects.create(user=request.user)
    add_writer.favorite_writers= writer_check
    add_writer.save()
    return messages.success(request, 'Writer added to your favorite list')
    


@login_required()
def shortlist_a_writer(request):
    pass

@login_required()
def decline_a_bid(request, bid_id):
    decline = Bids.objects.filter(bid_id=bidding_id).update(declined=True)
    return redirect(reverse('customer:index'))

    

class ViewAllWriters(LoginRequiredMixin,  ListView):
    template_name = 'users/writers/all_writers.html'
    model = WritersProfile
    context_object_name = 'writers'
    


def remove_from_favorite(request, writer_id):
    writer = get_object_or_404(FavouriteWriters, favorite_writers=writer_id)
    writer.delete()
    return redirect(reverse('customer:favorite_writers'))



class AgricWriters(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/agric.html'
   

class Culture(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/health.html'
  
    

class Economic(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/politic.html'
   

class LifeStyle(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/social.html'
    
    




