from django.contrib import admin
from django.urls import path, re_path, include
from direct import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('/', include('direct.urls')),
    path('accounts/', include('users.urls'))
]
