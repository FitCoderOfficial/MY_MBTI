from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mbti = models.CharField(max_length=4, blank=True)

class Test(models.Model):
    question = models.TextField()
    choices = models.JSONField()

class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.JSONField()