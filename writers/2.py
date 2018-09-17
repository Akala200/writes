from django.views.generic import CreateView, TemplateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import WriterSignupForm, WriterProfileForm
from .models import WritersProfile

    

class SignupView(CreateView):
    form_class = WriterSignupForm
    fields = ['email', 'full_name', 'topic_of_interest',  'resume']
    success_url = reverse_lazy('account-success-signup')
    template_name = ''

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


    def mail_site_admins(self):
        pass


class SuccessView(TemplateView):
    template_name = ''

    def dispatch(self, request, **kwargs):
        if 'success' not in request.session:
            return HttpResponseBadRequest('You cant access this page at this time')
        return super(SuccessView, self).dispatch(request, **kwargs)


class CreateProfile(LoginRequiredMixin, CreateView):
    form_class = WriterProfileForm
    model = WritersProfile
    template_name = ''
    fields = '__all__'

    def dispatch(self, request, *args, **kwargs):
        if not request.is_writer:
            return HttpResponseBadRequest()
        return super(CreateProfile, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile set up was successfully')
        else:
            messages.error(request, 'Failed to set up profile info')
            return form



class UpdateProfile(LoginRequiredMixin, UpdateView):
    form_class = WriterProfileForm
    template_name = ''
    model = WritersProfile

    
    def dispatch(self, request, *args, **kwargs):
        if not request.is_writer:
            return HttpResponseBadRequest()
        return super(UpdateProfile, self).dispatch(request, *args, **kwargs)
