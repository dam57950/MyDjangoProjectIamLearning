from django.db import models


# Create your models here.

class PhotoElement(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    description = models.TextField(default="Standard pics")
