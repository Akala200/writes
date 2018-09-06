from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import get_user_model


from allauth.account.forms import LoginForm



class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email']

    def signup(self, request, user):
        user.is_user = True
        user.save()


class LoginuserForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginuserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'input100'})
        self.fields['login'].widget.attrs.update({'class': 'input100'})
