from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_writer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    login_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)


