import os.path
import random

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import RegisterForm, ProfileForm, UsersFormMixin

from users.models import User
from django.contrib.auth.views import LoginView, LogoutView


class UserLogin(LoginView):
    template_name = 'users/login.html'


class UserLogout(LogoutView):
    pass


def rnd_url():
    new_url = "".join([str(random.randint(0, 9)) for _ in range(25)])
    new_url = 'verification/' + new_url
    return new_url


def var_url():
    # request.user.is_active = False
    valid_url_token = rnd_url()
    # request.user.valid_url_token = valid_url_token
    # request.user.save()
    return valid_url_token


# Регистрация пользователя
class RegisterView(CreateView):
    model = User
    # template_name = 'users/user_form.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    # def get_object(self, queryset=None):
    #     return self.request.user

    def post(self, request, *args, **kwargs):
        data = {
            'valid_url_token': var_url()
        }
        # request.user.valid_url_token = var_url()
        return render(request, 'users/login.html', context=data)

    def form_valid(self, form):
        new_user = form.save()
        print(new_user)
        print(new_user.is_active)
        # usr = self.get_object()
        form.valid_url_token = var_url()
        form.save()

        send_mail(
            subject='Поздравляем с регистрацией',
            message='Добро пожаловать на нашу платформу',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            # fail_silently=False,
            # auth_user=None,
            # auth_password=None,
            # connection=None,
            # html_message=None,
        )
        return super().form_valid(form)


class ProfileUpdate(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('catalog:index')
    template_name = 'users/profile_form.html'

    # переопределим метод, чтобы всегда редактировать текущего пользователя
    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_pass = User.objects.make_random_password()
    print(new_pass)
    print(request.user.email)
    request.user.set_password(new_pass)
    request.user.save()
    send_mail(
        subject='Смена пароля',
        message=f'Новый пароль: {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )

    return redirect(reverse('catalog:index'))
