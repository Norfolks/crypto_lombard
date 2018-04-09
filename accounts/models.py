from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.CharField(max_length=42, verbose_name='address')

    telegram = models.CharField(max_length=100, verbose_name='telegram')
    skype = models.CharField(max_length=100, verbose_name='skype')
    discord = models.CharField(max_length=100, verbose_name='discord')
