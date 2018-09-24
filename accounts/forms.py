from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from allauth.account.forms import ResetPasswordForm




class SignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input100', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'input100', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'input100', 'placeholder': 'Confirm-password'})
        

    def signup(self, request, user):
        user.is_writer = True
        user.save()

class LoginuserForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginuserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'input100'})
        self.fields['login'].widget.attrs.update({'class': 'input100'})


class ResetuserPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(ResetuserPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input100'})


        