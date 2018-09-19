from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import ValidationError


from .models import WritersProfile

class WriterSignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def save(self, commit=True):
        instance = super(WriterSignupForm, self).save(commit=False)
        if not instance.is_writer:
            instance.is_writer = True
            if commit:
                instance.save()
            return instance


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
