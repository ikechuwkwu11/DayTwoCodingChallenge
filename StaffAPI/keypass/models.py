from django.db import models
from datetime import timedelta
import uuid
from django.utils import timezone


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_authenticated(self):
        return True

class AccessToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=36,  default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() >self.created_at + timedelta(days=1)

    def __str__(self):
        return f'{self.user.username} - {self.token}'



