from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from portfolio.accounts.forms import LoginForm, RegisterForm


# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('hero')


    
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm


def logout_user(request):
    logout(request)
    return redirect('hero')
