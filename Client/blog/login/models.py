from django.db import models


# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    e = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    
