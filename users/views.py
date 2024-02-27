from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import RegisterForm, ProfileForm, UsersFormMixin
from users.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.models import User


class UserLogin(LoginView):
    template_name = 'users/login.html'


class UserLogout(LogoutView):
    pass


# Регистрация пользователя
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        new_user = form.save()
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
    request.user.set_password(new_pass)
    request.user.save()

    return redirect(reverse('users:profile'))


