import random
import json
from decimal import Decimal

import stripe

from django.shortcuts import render, redirect, reverse, resolve_url
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


from .forms import PaymentForm, PlaceAnOrderForm, CancelOrderForm,  AdditionalFileForm
from .models import (
    Wallet, WalletBalance, Order, FavouriteWriters,
    Hired, AdditionalFiles, ShortListed, InvitedWriters

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



class Index(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 10
    template_name = 'users/orders/all_user_orders.html'

    def get_queryset(self):
        queryset = Order.objects.filter(order_id=self.request.user).all()
        return queryset


@login_required()
def order_in_progress(request):
    order = Order.objects.filter(order_id=request.user, in_progress=True).all()
    return render(request, 'users/orders/in_progress.html', context={'orders':  order })

@login_required()
def cancelled_order(request):
    cancelled = Order.objects.filter(Q(order_id=request.user), Q(cancelled=True))
    return render(request, 'users/orders/cancelled.html', context={'orders':  cancelled }) 

@login_required()
def completed_order(request):
    order = Order.objects.filter(order_id=request.user, completed=True).all()
    return render(request, 'users/orders/completed_orders.html', context={'orders': order})

@login_required()
def expired_order(request):
    order = Order.objects.filter(order_id=request.user, expired=True).all()
    return render(request, 'users/orders/expired_order.html', context={'orders': order})

@login_required()
def place_an_order(request):
    form = PlaceAnOrderForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.order_id = request.user
            instance.order_uuid = generated_unique_id()
            
            form.save()
            messages.success(request, 'Your Order was created successfully')
            return redirect(reverse('customer:index'))


        else:
            messages.error(request, 'Failed to create an order')
            form = PlaceAnOrderForm()

    return render(request, 'users/orders/place_orders.html', context={
        'form': form
    })

@login_required()
def cancel_an_order(request, order_uuid):
    cancel_order = Order.objects.filter(order_uuid=order_uuid).update(cancelled=True)
    messages.success(request, 'Order cancelled successfully')
    return redirect(reverse('customer:index'))



@login_required()
def view_transactions(request):
    wallet = Wallet.objects.filter(wallet_id=request.user).order_by('-date')
    wallet_balance = WalletBalance.objects.get(balance_id=request.user)
    context = {'wallet': wallet, 'wallet_balance': wallet_balance}
    
    return render(request, 'users/wallet/wallet.html', context=context)

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
            payment_data = Wallet.objects.create(
                wallet_id = request.user,
                credit = amount,
                description = "Failed to process payment",
                declined = True
    
            )
            return redirect(reverse('customer:view_transactions'))
        
        except stripe.error.AuthenticationError:
            payment_data = Wallet.objects.create(
                wallet_id = request.user,
                credit = amount,
                description = "Failed to process payment",
                declined = True
    
            )
            return redirect(reverse('customer:view_transactions'))
    

        except stripe.error.InvalidRequestError:
            payment_data = Wallet.objects.create(
                wallet_id = request.user,
                credit = amount,
                description = "Failed to process payment",
                declined = True
    
            )
    

            
            return redirect(reverse('customer:view_transactions'))

        else:
            payment_data = Wallet.objects.create(
                wallet_id = request.user,
                credit = amount,
                description = description,
                approved = True
    
            )
            update_user_balance = WalletBalance.objects.filter(balance_id=request.user).update(balance=F('balance') + Decimal(amount))

            
            return redirect(reverse('customer:view_transactions'))
            
    return render(request, 'users/wallet/fund_wallet.html', context={'form': form,
    'stripe_key': stripe_key, 'amount': request.POST.get('amount')})
        


@login_required()
def order_details(request, order_uuid):
    form =   AdditionalFileForm()

    order_id = get_object_or_404(Order, order_uuid=order_uuid)
    files = AdditionalFiles.objects.filter(user=order_uuid).all()

    return render(request, 'users/bids/assignment_details.html', context={
        'bid':  order_id,
        'form': form,
        'files': files
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
        


    return render(request, 'users/orders/update_order.html', context={
        'form': form, 'order': order
    })
 


class AssignWriters(LoginRequiredMixin,  ListView):
    template_name = 'users/writers/all_writers.html'
    model = WritersProfile
    context_object_name = 'writers'


class DeclinedBids(LoginRequiredMixin, ListView):
    model = Bids
    context_object_name = 'declinedbids'
    paginate_by = 10
    template_name = 'users/bids/declined.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(Q(bidding_id=self.kwargs['order_uuid']), Q(declined=True))
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super(DeclinedBids, self).get_context_data(*args, **kwargs)
        context['bid'] = self.kwargs['order_uuid']
        return context


class ShortListedList(LoginRequiredMixin, ListView):
    model = ShortListed
    context_object_name = 'shortlist'
    paginate_by = 10
    template_name = 'users/bids/shortlisted.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(short_id=self.kwargs['order_uuid']).all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ShortListedList, self).get_context_data(*args, **kwargs)
        context['bid'] = self.kwargs['order_uuid']
        return context


   

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
    hire = Hired.objects.filter(user=request.user).all()
    return render(request, 'users/bids/hired_before.html', context={'hire':hire})



class Invited(LoginRequiredMixin,  ListView):
    model = InvitedWriters
    context_object_name = 'invite'
    paginate_by = 10
    template_name = 'users/bids/invited.html'


    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.kwargs['order_uuid']).all()
        return queryset


@login_required()
def invite_writers(request, order_uuid, writer_id):
    url = request.META.get('HTTP_REFERER')
    order_id = get_object_or_404(Order, order_uuid=order_uuid)
    writer_id = get_object_or_404(WritersProfile, pk=writer_id)
    from .utils import invite_writer
    context = {'order_id': order_id}
    invite = invite_writer(writer_id.profile_id.email, context)
    InvitedWriters.objects.create(user=order_id, invitees=writer_id)
    return redirect(resolve_url(url))
    


@login_required()
def new_bids(request):
    new_bids = Bids.objects.all().exclude(Q(approved=True), Q(shortlisted=True),
    Q(declined=True))
    return render(request, 'users/bids/new_bids.html')



@login_required()
def view_all_bids(request):
    bid = Bids.objects.all()
    return render(request, 'customer/bids/view_all_bids.html', context={'bid': bid})


@login_required
def additional_files(request, order_uuid):
    order_id =  url = request.META.get('HTTP_REFERER')
    AdditionalFiles.objects.filter(user=order_uuid).all()
    return render(request, 'te', context={'order': order_id, 'order_id': order_uuid})


@login_required
def add_additional_file(request, order_uuid):
    url = request.META.get('HTTP_REFERER')
    form = AdditionalFileForm(request.POST, request.FILES)

    if  request.method == 'POST' and  form.is_valid():
        order = Order.objects.get(order_uuid=order_uuid)
        instance = form.save(commit=False)
        instance.user = order
        instance.save()
        messages.success(request, 'File submitted sucessfully')
        return redirect(resolve_url(url))

    else:
        return redirect(resolve_url(url))


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


    return render(request, 'users/orders/place_orders.html', context={
        'form': form, 'order': order
    })


@login_required()
def add_to_favorite(request, writer_id):
    url = request.META.get('HTTP_REFERER')
    writer_check = get_user_model().objects.get(user_profile__pk=writer_id)
    add = FavouriteWriters.objects.create(user=request.user, favorite_writers=writer_check,
    is_fav=True)

    return redirect(resolve_url(url))
    


@login_required()
def shortlist_a_writer(request):
    pass

@login_required()
def decline_a_bid(request, bid_id):
    decline = Bids.objects.filter(bid_id=bid_id).update(declined=True)
    return redirect(reverse('customer:index'))

    

class ViewAllWriters(LoginRequiredMixin,  ListView):
    template_name = 'users/writers/all_writers.html'
    model = WritersProfile
    context_object_name = 'writers'

    def queryset(self):
        query = WritersProfile.objects.exclude(is_approved=False).all()
    


def remove_from_favorite(request, writer_id):
    writer = FavouriteWriters.objects.filter(favorite_writers=writer_id).delete()
    return redirect(reverse('customer:favorite_writers'))



class AgricWriters(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/agric.html'
   

class Culture(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/health.html'
  
    

class Economic(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/politic.html'
   

class LifeStyle(LoginRequiredMixin, TemplateView):
    template_name = 'users/writers/social.html'
    

@login_required()
def place_order_for_a_writer(request, writer_id):
    pass



