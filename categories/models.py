from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    types = [
        ('Expense Category','Expense Category'),
        ('Income Category','Income Category'),
    ]

    type = models.CharField(max_length=50,choices=types,default='Income Category')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
