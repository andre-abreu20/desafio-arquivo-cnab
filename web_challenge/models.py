from django import forms
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    content = models.FileField()

    # def __str__(self):
    #     return self.content
