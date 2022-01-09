from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    name = models.CharField(max_length=80)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
