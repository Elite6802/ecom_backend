from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Now that we have created the email, we use it as a login identifier and not the username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]

    def __str__(self):
        return self.email