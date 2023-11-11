from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    path('users/', views.user_list, name="user_list"),
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('logout/', views.logout, name="logout"),
    path('entries/', views.entry_list, name="entry_list"),
]
