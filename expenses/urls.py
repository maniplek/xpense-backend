from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
app_name = 'expenses'

urlpatterns = [
    path('get_expenses/', views.ExpenseList.as_view(), name='get_expenses'),
    path('update_expense/<slug:pk>', views.ExpenseDetail.as_view(), name='update_expense'),

    path("create_expense/", views.create_expense, name="create_expense"),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)