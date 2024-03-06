import os.path
import random

# from django.contrib.auth import get_user
from django.contrib.sites.shortcuts import get_current_site

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView

from config import settings
from users.forms import RegisterForm, ProfileForm, UsersFormMixin, VerifyForm

from users.models import User
from django.contrib.auth.views import LoginView, LogoutView


class UserLogin(LoginView):
    template_name = 'users/login.html'


class UserLogout(LogoutView):
    pass


def rnd_url():
    token = "".join([str(random.randint(0, 9)) for _ in range(25)])
    new_url = "http://localhost:8000/" + token
    # return new_url
    return token


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'user_id': user.pk,
        'domain': current_site.domain,
        'token': rnd_url(),
    }
    end_url = f'http://{context["domain"]}/{context["user_id"]}/{context["token"]}'

    send_mail(
        subject='Поздравляем с регистрацией',
        message=f'Добро пожаловать на нашу платформу.\n'
                f'Ссылка для подтверждения регистрации: {end_url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        # fail_silently=False,
        # auth_user=None,
        # auth_password=None,
        # connection=None,
        # html_message=None,
    )


# def var_url():
#     valid_url = rnd_url()
#     return valid_url


# Регистрация пользователя
class RegisterView(CreateView):
    model = User
    # template_name = 'users/user_form.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    # def get_object(self, queryset=None):
    #     return self.request.user

    def form_valid(self, form):
        new_user = form.save()
        # print(new_user)
        # print(new_user.is_active)
        # print(new_user.valid_url_token)
        # print('-' * 50)

        new_user.is_active = False
        new_user.valid_url_token = rnd_url()

        # print(new_user.is_active)
        # print(new_user.valid_url_token)
        # form = new_user
        # form.save()

        # usr = self.get_object()
        # print(usr.is_active)
        # form.valid_url_token = var_url()
        # form.save()
        send_email_for_verify(self.request, new_user)

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


# def verify_email(request):
#     data = {
#         'title': 'Подтверждение почты'
#     }
#     user_data = request.user
#     if not user_data.is_active:
#         user_data.is_active = True
#
#     return render(request, 'users/login.html', context=data)


class VerifyTemplateView(TemplateView):
    model = User
    form_class = VerifyForm
    template_name = 'users/confirm_email.html'
    success_url = reverse_lazy('users:login')

    # def get_object(self, queryset=None):
    #     return self.request.user

    def get_user(self, user_id, token):
        user = User.objects.filter(pk=user_id, valid_url_token=token)
        return user[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = context['user_id']
        token = context['token']
        user = self.get_user(user_id, token)
        print(user)


        # if usr:
        #     print(usr.object)
        #     # print(f"{usr.email} - {usr.is_active}")
        return context

    # def post(self, request, *args, **kwargs):
    #     # current_url = get_current_site(request)
    #     data = {}
    #     current_url = request.path
    #     current_url = current_url.split('/')
    #     data['pk'] = current_url[1]
    #     data['valid_url_token'] = current_url[2]
    #     print(f'pk = {data["pk"]}\nvalid_url_token = {data["valid_url_token"]}')
    #
    #     obj = User.objects.filter(pk=data['pk'])
    #     print(obj.__dict__)
    #     for i in obj:
    #         print(i)
    #     # if obj['valid_url_token'] == data['valid_url_token']:
    #     #     obj['is_active'] = True
    #     #     print('User - активирован')
    #     #     obj.save()
    #     return super().post(request, *args, **kwargs)
    #     # return render(request, 'users/confirm_email.html', context=data)
