from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=13)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
