from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import ValidationError


from allauth.account.forms import SignupForm

from .models import WritersProfile

class WriterSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(WriterSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input100', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'input100', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'input100', 'placeholder': 'Confirm-password'})
        self.fields['email'].error_messages['required'] = 'This email exist with an account already'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = WritersProfile
        fields = ('image', 'headline', 'subject_one',
        'subject_two', 'subject_three', 'about')


class EssayTestForm(forms.Form):
    test = forms.CharField(widget=forms.Textarea())

    def clean_test(self):
        if len(self.cleaned_data['test']) == 250:
            raise ValidationError('Too Short')
        return self.cleaned_data['test']
