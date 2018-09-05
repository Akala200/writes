from allauth.account.views import LoginView

class Login(LoginView):
    template_name = 'accounts/login.html'