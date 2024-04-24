from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField("Name", max_length=50)
    lname = models.CharField("Last Name", max_length=50)
    bio = models.TextField()
    job = models.CharField(max_length=404)
    avatar = models.ImageField(upload_to='avatars/')

