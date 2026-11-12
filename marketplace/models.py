from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    USER_TYPES = [
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPES
    )

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"