from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
app_name = 'users'

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users_list'),
    path('user_update/<slug:pk>', views.UserDetail.as_view(), name='users_detail'),


    path("login/", views.login, name="auth_token_login"),
    path("change_password/", views.change_password, name="change_password"),
    path("user_register/", views.user_register, name="user_register"),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)