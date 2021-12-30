from django.db import models
from income.models import Income
from expenses.models import Expense
from accounts.models import Account
from users.models import User

# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True, blank=True)
    income = models.ForeignKey(Income, on_delete=models.CASCADE,  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.account)

class Preference(models.Model):
    amout_limit = models.IntegerField(blank=True, default=200000)
    default_currency = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.amout_limit