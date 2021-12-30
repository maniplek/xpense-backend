from django.db import models
from users.models import User

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    currencies = [
        ('RWF','RWF'),
        ('$','$'),
    ]

    currency = models.CharField(max_length=50,choices=currencies, default='RWF')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)