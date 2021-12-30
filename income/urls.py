from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
app_name = 'income'

urlpatterns = [
    path('get_income/', views.IncomeList.as_view(), name='get_income'),
    path('update_income/<slug:pk>', views.IncomeDetail.as_view(), name='update_income'),

    path("create_income/", views.create_income, name="create_income"),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)