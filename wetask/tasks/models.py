from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    end_by = models.DateField(default=None, null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )
