from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    path('users/', views.user_list, name="user_list"),
]
