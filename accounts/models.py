from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
