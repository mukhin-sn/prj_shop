from django.db import models
from django.contrib.auth.models import AbstractUser

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='превью', **NULLABLE)
    phone = models.CharField(max_length=16, verbose_name='', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
