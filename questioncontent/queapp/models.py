from django.db import models


class Content(models.Model):
    entry = models.TextField(unique=True)

class Question(models.Model):
    que = models.TextField(unique=True)
    subject = models.TextField()
    difficulty = models.TextField()
    ref = models.ForeignKey(Content)
# Create your models here.
