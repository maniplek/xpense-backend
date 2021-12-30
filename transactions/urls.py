from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
app_name = 'transactions'

urlpatterns = [
    path('get_transactions/', views.TransactionList.as_view(), name='get_income'),
    path("get_transactions_by_account/", views.get_transactions_by_account, name="create_expense"),
    path("get_transactions_by_range/", views.get_transactions_range, name="create_expense"),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)