from django.db import models
from django.contrib.auth.models import AbstractUser

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=16, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
