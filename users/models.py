from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User (AbstractUser):
    username = None
    groups = None
    first_name = None
    last_name = None


    full_name = models.CharField(_('Full Name'),max_length=100)
    email = models.EmailField(_('Email'),unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name
    