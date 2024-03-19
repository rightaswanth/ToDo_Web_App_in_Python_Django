# users/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .import views


urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register_view,name='register')
]
