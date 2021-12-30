from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.response import Response

# Create custom model.

class User(AbstractUser):
    name = models.CharField(max_length=200, unique=False,)
    phone_number = models.CharField(max_length = 20,blank=True, null=True, default='')
    profile_pic = models.TextField(blank=True, null=True, default='')
    email = models.EmailField('email address', unique = True)
    username = models.CharField(max_length=40, unique=False, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return "{}".format(self.email)
