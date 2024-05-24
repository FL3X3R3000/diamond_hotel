from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
    path('rooms/', views.rooms, name='rooms'),
    path('booking/<int:room_id>/', views.book, name='booking'),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
