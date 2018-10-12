import random
import json
from decimal import Decimal

import paypalrestsdk


from django.shortcuts import render, redirect, reverse, resolve_url
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import F, Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, FormView


from .forms import (PaymentForm, PlaceAnOrderForm, CancelOrderForm,  
AdditionalFileForm, RatingForm, RateForm )
from .models import (

    Wallet, WalletBalance, Order, FavouriteWriters,
    Hired, AdditionalFiles

)

from writers.models import Bids, WritersProfile, InvitedWriters


from .utils import invite_writer


paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AU3T5D2sAeqacb1Hmp6jJybSun7vJFNpC8YiG_WJEfFiISZeu1Fb-5hd_oQLzF9uubScMTdAhUsBaSws",
  "client_secret": "EDydVe55CAAhArVT6WbTcJz8O8c0xOKjCVKSUx1Ooc7EwG0VukBKvLDJopg6VmA65G6BbfsSLTUHmFtu" })


def generated_unique_id():
    ran = ''.join(str(random.randint(2, 8)) for x in range(6))
    return ran



class Index(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 10
    template_name = 'users/orders/all_user_orders.html'

    def get_queryset(self):
        queryset = Order.objects.filter(order_id=self.request.user).order_by('-deadline')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['cancelled'] = False
        for query in self.get_queryset():
            context['offers'] = query.offer_id.offers
            if query.cancelled:
                print(True)
                context['cancelled'] = True
                
        return context


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
            
            instance.save()
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

    form = PaymentForm(request.POST)
    if request.method == "POST" and form.is_valid():
        amount = form.cleaned_data['amount']
        payment = paypalrestsdk.Payment({
            "intent": "sale",
             "payer": {
                 "payment_method": "paypal"},
                 "redirect_urls": {
                     "return_url": request.build_absolute_uri(reverse('customer:execute_payment')),
                     "cancel_url": request.build_absolute_uri(reverse('customer:cancel_payment'))},
                     "transactions": [{
                         "item_list": {
                             "items": [{
                                 "name": "item",
                                 "sku": "item",
                                 "price": amount,
                                 "currency": "USD",
                                 "quantity": 1}]},
                                 "amount": {
                                     "total": amount,
                                     "currency": "USD"},
                                     "description": "This is the payment transaction description."}
            ]})
        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    request.session['amount'] = amount
                    approval_url = str(link.href)
                    return redirect(approval_url)
        else:
            print(payment.error)
    return render(request, 'users/wallet/fund_wallet.html', context={'form': form,
   'amount': request.POST.get('amount')})


@login_required()
def execute_payment(request):
    amount  = request.session.get('amount', '')
    payerID = request.GET.get('PayerID', None)
    paymentID = request.GET.get('paymentId', None)
    if payerID is None and paymentID is None:
        return redirect(reverse('customer:view_transactions'))

    payment = paypalrestsdk.Payment.find(paymentID)
    if payment.execute({"payer_id":  payerID}):
        Wallet.objects.create(
            wallet_id=request.user,
            description = 'Payment Via Paypal',
            approved = True,
            credit  = Decimal(amount)
        )

        WalletBalance.objects.filter(balance_id=request.user).update(balance=F('balance') + Decimal(amount))
        del request.session['amount']
        return redirect(reverse('customer:view_transactions'))
        
    else:
        Wallet.objects.create(
            wallet_id=request.user,
            description = 'Payment Failed',
            declined = True,
            credit  = Decimal(amount)
            )
        del request.session['amount']
        return redirect(reverse('customer:view_transactions'))
        

@login_required()
def cancel_payment(request):
    amount = request.session.get('amount',  '')
    if amount != '':
        Wallet.objects.create(
            wallet_id=request.user,
            description = 'Payment Failed',
            declined = True,
            credit  = Decimal(amount)
            )
        del request.session['amount']
        return redirect(reverse('customer:view_transactions'))


@login_required()
def order_details(request, order_uuid):
    order_id = get_object_or_404(Order, order_uuid=order_uuid)
  
    bids  = Bids.objects.filter(bidding_id=order_id).order_by('-date_created')

    for bid in bids:
        if bid.approved:
            form = RateForm()
            return render(request, 'users/bids/hiredwriter.html', context={
                'order': order_id.order_uuid,
                'form':  form
                })

   
    return render(request, 'users/bids/all_bids.html', context={
        'bids':  bids,
        'order': order_id.order_uuid
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
    template_name = 'users/bids/assign_writer.html'
    model = WritersProfile
    context_object_name = 'writers'

    def get_queryset(self):
        query = WritersProfile.objects.exclude(is_approved=False).all()
        return query
        
    def get_context_data(self, *args, **kwargs):
        context = super(AssignWriters, self).get_context_data(*args, **kwargs)
        context['order'] = self.kwargs['order_uuid']
        return context


class DeclinedBids(LoginRequiredMixin, ListView):
    model = Bids
    context_object_name = 'declined_bids'
    paginate_by = 10
    template_name = 'users/bids/declined.html'

    def get_queryset(self):
        order_uuid = Order.objects.get(order_uuid=self.kwargs['order_uuid'])
        queryset = self.model.objects.filter(Q(bidding_id=order_uuid), Q(declined=True))
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super(DeclinedBids, self).get_context_data(*args, **kwargs)
        context['order'] = self.kwargs['order_uuid']
        return context


class ShortListedList(LoginRequiredMixin, ListView):
    model = Bids
    context_object_name = 'shortlist_bid'
    paginate_by = 10
    template_name = 'users/bids/shortlisted.html'

    def get_queryset(self):
        order_uuid = Order.objects.get(order_uuid=self.kwargs['order_uuid'])
        queryset = self.model.objects.filter(bidding_id=order_uuid, 
        shortlisted=True).all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ShortListedList, self).get_context_data(*args, **kwargs)
        context['order'] = self.kwargs['order_uuid']
        return context



def remove_from_shortlist(request, bid_id, order_uuid):

    decline = Bids.objects.filter(pk=bid_id).update(shortlisted=False)
    return redirect(reverse('customer:order_detail', kwargs={
        'order_uuid': order_uuid
    }))

   

class CompletedBids(LoginRequiredMixin,  ListView):
    model = Bids
    context_object_name = 'bids'
    paginate_by = 10
    template_name = 'customer/bids/completed.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(Q(order_uuid=self.request.user), Q(completed=True))
        return queryset


class HiredBefored(LoginRequiredMixin,  ListView):
    model = Hired
    context_object_name = 'hired'
    paginate_by = 10
    template_name = 'users/bids/hired_before.html'


    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user).all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(HiredBefored, self).get_context_data(*args, **kwargs)
        context['order'] = self.kwargs['order_uuid']
        return context



class Invited(LoginRequiredMixin,  ListView):
    model = InvitedWriters
    context_object_name = 'invited_writer'
    paginate_by = 10
    template_name = 'users/bids/invited.html'


    def get_queryset(self):
        order = Order.objects.get(order_uuid=self.kwargs['order_uuid'])
        queryset = self.model.objects.filter(user=order).all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Invited, self).get_context_data(**kwargs)
        context['order'] = self.kwargs['order_uuid']
        return context


@login_required()
def invite_writers(request, order_uuid, writer_id):
    url = request.META.get('HTTP_REFERER')
    order_id = get_object_or_404(Order, order_uuid=order_uuid)
    writer_id = get_object_or_404(WritersProfile, pk=writer_id)
    context = {'order_uuid': order_id}
    invite = invite_writer(writer_id.profile_id.email, **context)
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
    order = get_object_or_404(Order, order_uuid=order_uuid)
    files = AdditionalFiles.objects.filter(user=order)
    
    return render(request, 'users/bids/additional_files.html', context={'order': order_uuid, 'files': files})
    


@login_required
def add_additional_file(request, order_uuid):
    form = AdditionalFileForm(request.POST, request.FILES)
    if  request.method == 'POST' and  form.is_valid():
        order = get_object_or_404(Order, order_uuid=order_uuid)
        instance = form.save(commit=False)
        instance.user = order
        instance.save()
        messages.success(request, 'File submitted sucessfully')
        return redirect(reverse('customer:additional_files', kwargs={'order_uuid': order_uuid}))

    else:
        return HttpResponseBadRequest('something bad happened')


class FavoriteWriter(LoginRequiredMixin,  ListView):
    template_name = 'users/writers/favorite.html'
    model = FavouriteWriters
    paginate_by = 10
    context_object_name = 'favorite'


    def get_queryset(self):
        queryset =  self.model.objects.filter(user=self.request.user).all()
        return queryset



class FavoriteWriterBids(LoginRequiredMixin,  ListView):
    template_name = 'users/bids/favorite_writers.html'
    model = FavouriteWriters
    paginate_by = 10
    context_object_name = 'favorite'


    def get_queryset(self):
        queryset =  self.model.objects.filter(user=self.request.user).all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FavoriteWriterBids , self).get_context_data(**kwargs)
        context['order'] = self.kwargs['order_uuid']
        return context



@login_required()
def resubmit_order(request, order_uuid):
    order = get_object_or_404(Order, order_uuid=order_uuid)
    form = PlaceAnOrderForm(request.POST, instance=order)
    if request.method == "POST":
        if form.is_valid():
            order.delete()
            instance = form.save(commit=False)
            instance.order_id = request.user
            instance.order_uuid = generated_unique_id()    
            instance.save()
            messages.success(request, 'Order submited')
            return redirect(reverse('customer:order_detail', kwargs={'order_uuid': instance.order_uuid}))
        
    else:
        form = PlaceAnOrderForm(instance=order)


    return render(request, 'users/orders/resubmit_order.html', context={
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
def shortlist_a_bid(request, bid_id, order_uuid):
    
    decline = Bids.objects.filter(pk=bid_id).update(shortlisted=True)
    return redirect(reverse('customer:short_listed', kwargs={
        'order_uuid': order_uuid
    }))

@login_required()
def decline_a_bid(request, bid_id, order_uuid):
   
    decline = Bids.objects.filter(pk=bid_id).update(declined=True)
    return redirect(reverse('customer:declined', kwargs={
        'order_uuid': order_uuid
    }))

    

class ViewAllWriters(LoginRequiredMixin,  ListView):
    template_name = 'users/writers/all_writers.html'
    model = WritersProfile
    context_object_name = 'writers'

    def queryset(self):
        query = WritersProfile.objects.exclude(is_approved=False).all()
        return query
    


def remove_from_favorite(request, writer_id):
    url = request.META.get('HTTP_REFERER')
    FavouriteWriters.objects.filter(favorite_writers=writer_id).delete()
    return redirect(resolve_url(url))



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
    form = PlaceAnOrderForm(request.POST)
    if form.is_valid() and request.method == "POST":
        instance = form.save(commit=False) 
        instance.order_id = request.user
        instance.order_uuid = generated_unique_id()
        instance.save()        
        writer = get_object_or_404(WritersProfile, pk=writer_id)
        instance.mail_writers(writer.profile_id.email)
        messages.success(request, 'Your Order was created successfully')
        return redirect(reverse('customer:index'))

    form = PlaceAnOrderForm()
    return  render(request, 'place_order_for_a_writer.html', context={
        'form': form
    })
 
class RateWriter(LoginRequiredMixin, FormView):
    form_class = RatingForm
    

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.rating_id = self.request.user
        instance.rater = self.kwargs['writer_id']
        instance.save()
        return redirect(resolve_url(self.request.META.get('HTTP_REFERRAL')))

    
@login_required()
def bidding_order(request, order_uuid):
    form =   AdditionalFileForm()
    order_id = get_object_or_404(Order, order_uuid=order_uuid)
    
    return render(request, 'users/bids/bidding_detail.html', context={
        'bid':  order_id,
        'form': form,
        'order': order_id.order_uuid
        })



@login_required()
def delete_uploaded_file(request, file_id):
    url = request.META.get('HTTP_REFERER')
    AdditionalFiles.objects.filter(id=file_id).delete()
    return redirect(resolve_url(url))


@login_required()
def hired_writer(request, order_uuid):
    order_id = get_object_or_404(Order, order_uuid=order_uuid)

    return render(request, 'users/bids/hiredwriter.html', context={
        'order': order_id.order_uuid
    })