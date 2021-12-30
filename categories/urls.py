from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
app_name = 'categories'

urlpatterns = [
    path('get_categories/', views.CategoryList.as_view(), name='get_categories'),
    path('update_category/<slug:pk>', views.CategoryDetail.as_view(), name='update_category'),

    path("create_category/", views.create_category, name="create_category"),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)