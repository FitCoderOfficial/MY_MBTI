from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mbti = models.CharField(max_length=4, null=True, blank=True)
    shared_link = models.CharField(max_length=255, null=True, blank=True)