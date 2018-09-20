from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, reverse
from django.contrib.messages import success, error
from allauth.account.views import LoginView
from .forms import LoginuserForm


class LoginUserView(LoginView):
    form_class = LoginuserForm
    template_name = 'account/login.html'

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            user = authenticate(self.request, user=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_user:
                    login(self.request, user)
                    return redirect(reverse('customer:index'))
                else:
                    login(self.request, user)
                    return redirect(reverse('writers:home'))
            return error(self.request, 'invalid credentails')