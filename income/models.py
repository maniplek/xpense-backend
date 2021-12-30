from django.db import models
from users.models import User
from categories.models import Category

# Create your models here.

class Income(models.Model):
    amount = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=200, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)