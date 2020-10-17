from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address', max_length=255, unique=True)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
