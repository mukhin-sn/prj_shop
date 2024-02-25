from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm
from users.models import User
from django.contrib.auth.views import LoginView, LogoutView


class UserLogin(LoginView):
    template_name = 'users/login.html'


class UserLogout(LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

