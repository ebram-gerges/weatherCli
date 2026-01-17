from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=500)
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_full_name()}"
