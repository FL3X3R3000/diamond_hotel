from django.contrib import admin
from django.urls import path, re_path, include
from . import views
urlpatterns = [
    re_path('login/', views.sign_in, name='signin'),
    re_path('logout/', views.sign_out, name='signout'),
    re_path('register/', views.sign_up, name='signup')
]