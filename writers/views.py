from django.views.generic import CreateView, TemplateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import WriterSignupForm, ProfileForm
from .models import WritersProfile

    

def signup(request):
    form =  WriterSignupForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('')
    else:
        return render(request, 'writers/accounts/signup.html')


@login_required()
def create_profile(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.profile_id = request.user
        instance.save()
        messages.success(request, 'Your profile set up was successfully')
        return redirect(reverse(''))
    
    else:
        form =  ProfileForm()
        return render(request, 'writers/home.html', context= {
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
        return redirect()
    
    else:
        form =  ProfileForm()
        return render(request, 'writers/home.html', context = {
            'form': form
        })


@login_required()
def set_up_payment_system(request):
    pass