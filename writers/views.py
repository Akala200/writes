from django.views.generic import CreateView, TemplateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , get_user_model, authenticate
from django.contrib.auth.backends import ModelBackend

 
from .forms import WriterSignupForm, ProfileForm, EssayTestForm
from .models import WritersProfile

    

def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse('writers:home'))
    else:
        form =  WriterSignupForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save(request)
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            if user:
                login(request, user)
                return redirect(reverse('writers:home'))
        else:
            form =  WriterSignupForm()
            return render(request, 'writers/accounts/signup.html', context={
                'form': form })

@login_required()
def home(request):
    return render(request, 'writersnew/intro.html')

class AllOrders(LoginRequiredMixin, TemplateView):
    template_name = 'writersnew/orders/all_orders.html'
    paginate_by = 5

    def get_context_data(self):
        pass


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
    form = ProfileForm(request.POST)
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


@login_required()
def update_profile(request):
    form = ProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.profile_id = request.user
        instance.save()
        messages.success(request, 'Your profile set up was successfully')
        return redirect(reverse('writers:home'))
    
    else:
        form =  ProfileForm()
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