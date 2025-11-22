from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'admin'
    CUSTOMER = 'customer'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER,
    )

    # Now that we have created the email, we use it as a login identifier and not the username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]

    def __str__(self):
        return self.email