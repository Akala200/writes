from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , get_user_model, authenticate
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist

from customer.models import Wallet, WalletBalance, Order
 
from .forms import WriterSignupForm, ProfileForm, EssayTestForm, UploadFile
from .models import WritersProfile, Bids, AssignmentFiles


    

def signup(request):
    try:
        if request.user.is_authenticated and request.user.user_profile.is_writer:
            return redirect(reverse('writers:all_orders'))
    except ObjectDoesNotExist:
        pass
    except request.user.is_authenticated:
        pass
    form =  WriterSignupForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save(request)
        user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        if user:
            WritersProfile.objects.create(profile_id=user, is_writer=True)
            login(request, user)
            return redirect(reverse('writers:home'))
    else:
        form =  WriterSignupForm()
        return render(request, 'writers/accounts/signup.html', context={'form': form })

<<<<<<< HEAD:writers/views.py
=======
    def post(self, request, kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False) 
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            self.mail_site_admins()
            request.session['success'] = True
            form.save()
        else:
            return form
>>>>>>> bc7096aeb3e579581087bf86975386068f4fba7f:writers/2.py

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'writersnew/intro.html'


class AllBids(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orders/all_orders.html'
    paginate_by = 5
    queryset = Bids
    context_object_name = 'bids'

    def get_queryset(self):
        queryset = self.queryset.objects.filter(bidders=self.request.user)
        return queryset

@login_required()
def bidding_orders(request):
    return render(request, 'writers/view/all_orders.html')

@login_required()
def in_progress(request):
    return render(request, 'writers/view/all_orders.html')

@login_required()
def new_orders(request):
    return render(request, 'writers/view/new_orders.html')

@login_required()
def personal(request):
    return render(request, 'writers/view/personal.html.html')


@login_required()
def create_profile(request):
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.profile_id = request.user
        instance.save()
        messages.success(request, 'Your profile set up was successfully')
        return redirect(reverse('writers:home'))
    
    else:
        form =  ProfileForm()
        return render(request, 'writersnew/add_profile.html', context= {
            'form': form
        })

class UpdateInfo(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = WritersProfile
    pk_url_kwarg = 'writer_id'
    template_name = 'writersnew/update_profile.html'
    success_url = reverse_lazy('writers:home')


@login_required()
def update_profile(request):
    user = get_user_model().objects.get(email=request.user)
    form = ProfileForm(request.POST, request.FILES, instance=request.user.user_profile)
    
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile_id = request.user
            messages.success(request, 'Your profile set up was successfully')
            return redirect(reverse('writers:home'))

        else:
            return HttpResponseBadRequest('bad news')
    
    else:
        form =  ProfileForm(instance=user)
        return render(request, 'writersnew/update_profile.html', context = {
            'form': form
        })

@login_required()
def write_an_essay(request):
    form = EssayTestForm(request.POST)
    if request.method == "POST" and form.is_valid() :
        pass
    else:
        form =  EssayTestForm()
    return render(request, 'writers/take_a_essay.html', context={
        'form': form
    })

@login_required()
def answer_question(request):
    pass


@login_required()
def writer_profile_detail(request, writer_name):
    writer_info  = get_object_or_404(WritersProfile, full_name=writer_name)
    return render(request, '', context={
        'detail': writer_info 
    })



@login_required()
def view_transactions(request):
    wallet = Wallet.objects.filter(wallet_id=request.user).order_by('-date')
    wallet_balance = WalletBalance.objects.get(balance_id=request.user)
    context = {'wallet': wallet, 'wallet_balance': wallet_balance}
    
    return render(request, 'writersnew/wallet/wallet.html', context=context)


class  NewOrders(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orders/new_order.html'
    queryset = Order
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = self.queryset.objects.filter(subject__in=self.request.user.user_profile.subject).exclude(in_progress=True).exclude(cancelled=True).exclude(
            expired=True
        ).order_by('-publication_date')
        
        return queryset
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['bid_placed'] = False       
       
    
        return context
    

def order_details(request, order_uuid):
    order = Order.objects.get(order_uuid=order_uuid)
    file = order.additional_filesc.filter(user=order)
    
   
    return render(request, 'writersnew/orders/view_order_details.html', context={'bid': order, 
    'files': file})


class CompletedOrders(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orders/completed_order.html'
    queryset = Bids
    context_object_name = 'bids'

    def get_queryset(self):
        queryset = Bids.objects.filter(bidders=self.request.user, completed=True).order_by(
            '-date_created'
        )
        return queryset 

class ExpiredOrders(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orders/expired_order.html'
    context_object_name = 'bids'
    queryset = Bids

    def get_queryset(self):
        queryset =  Bids.objects.filter(bidders=self.request.user, expired=True).order_by(
            '-date_created'
        )
        return queryset



class CancelledOrders(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orders/cancelled.html'
    context_object_name = 'bids'
    queryset = Bids

    def get_queryset(self):
        queryset =  Bids.objects.filter(bidders=self.request.user, cancelled=True).order_by(
            '-date_created'
        )
        return queryset



class BidsProgress(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orders/in_progress.html'
    context_object_name = 'bids'
    queryset = Bids

    def get_queryset(self):
        queryset =  Bids.objects.filter(bidders=self.request.user, approved=True).order_by(
            '-date_created'
        )
        return queryset

@login_required()
def place_a_bid(request, order_uuid):
    order =  Order.objects.get(pk=order_uuid)
    #order = get_object_or_404(Order, pk=order_uuid)
    order.bid_placed = True
    order.save()
   
    
    Bids.objects.create(
        bidding_id=order,
        bidders=request.user,
        amount=25.00,
        
    )
    return redirect(reverse('writers:all_orders'))

class BidInProgressDetaill(LoginRequiredMixin, DetailView):
    queryset = Order
    template_name = 'writersnew/orders/view_order_in_progress.html'
    context_object_name = 'bid'

    def get_object(self):
        queryset = get_object_or_404(self.queryset, order_uuid=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['files'] =  self.get_object().additional_filesc.filter(user=self.get_object())
        context['bid_order'] = self.kwargs['pk']
        context['bid_pk'] = get_object_or_404(Bids, bidding_id=self.get_object().pk)
        return context

class UploadedAssignmentFile(CreateView):
    template_name=''
    

@login_required()
def upload_assignment_file(request, bid_id):
    url = request.META.get('HTTP_REFERRAL')
    bid = get_object_or_404(Bids, pk=bid_id)
    form = UploadFile(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.file_id = bid
        instance.save()
        return redirect(resolve_url(url))
    return redirect(resolve_url(url))

class ViewAssignment(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orderS/view_files.html'
    queryset = AssignmentFiles
    context_object_name = 'files'

    def get_queryset(self):
        order =  get_object_or_404(Order, order_uuid=self.kwargs['pk'])
        self.bid_id = get_object_or_404(Bids, bidding_id=order.pk)
        
        query = self.queryset.objects.filter(file_id=self.bid_id).order_by('-pk')
        
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bid_order'] = self.kwargs['pk']
        context['bid_pk'] = self.bid_id
        return context

@login_required()
def delete_uploaded_file(request, file_id):
    url = request.META.get('HTTP_REFERER')
    AssignmentFiles.objects.filter(id=file_id).delete()
    return redirect(resolve_url(url))
