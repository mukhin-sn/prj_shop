from django import forms

from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UsersFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RegisterForm(UsersFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'phone', 'avatar', 'country',)


class ProfileForm(UsersFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    # Скрываем поле пароля в форме
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
