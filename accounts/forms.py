from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from allauth.account.forms import LoginForm, SignupForm


class SignupuserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 
    'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 
    'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 
    'Password'}))

    class Meta:
        model = get_user_model()
        fields = ['email']

    def signup(self, request, user):
        pass



class LoginuserForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginuserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'input100'})
        self.fields['login'].widget.attrs.update({'class': 'input100'})
