from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=50)
    date_of_birth = models.CharField(max_length=100)
    occupation = models.CharField(max_length=50)
