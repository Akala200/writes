from django.views.generic import CreateView, TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , get_user_model, authenticate
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist
 
from .forms import WriterSignupForm, ProfileForm, EssayTestForm
from .models import WritersProfile, Bids

    

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

@login_required()
def home(request):
    return render(request, 'writersnew/intro.html')

class AllOrders(LoginRequiredMixin, ListView):
    template_name = 'writersnew/orders/all_orders.html'
    paginate_by = 5
    queryset = Bids

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


class UpdateProfile(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm()
    template_name = 'writersnew/update_profile.html'
    model = WritersProfile



@login_required()
def update_profile(request):
    user = get_user_model().objects.get(email=request.user)
    form = ProfileForm(request.POST, request.FILES, instance=user)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
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