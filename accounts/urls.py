from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
app_name = 'accounts'

urlpatterns = [
    path('get_accounts/', views.AccountList.as_view(), name='get_accounts'),
    path('update_account/<slug:pk>', views.AccountDetail.as_view(), name='update_account'),

    path("create_account/", views.create_account, name="create_account"),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)