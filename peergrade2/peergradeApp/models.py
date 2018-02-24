from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.


class Notification(models.Model):
    sender = models.CharField(max_length=64)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now())
    active = models.BooleanField()
    request_moderation = models.BooleanField(default=False)

