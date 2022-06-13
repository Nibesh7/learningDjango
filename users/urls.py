
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as authentication_view

app_name = 'users' #namespacing urls
urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', authentication_view.LoginView.as_view(template_name='users/login.html'),name='login'),
   
]
