from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    
    is_writer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    topic_of_interest = models.CharField(max_length=150, null=True)
    resume = models.ImageField(null=True)
    full_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)
    is_active   = models.BooleanField(default=True)
    login_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)


