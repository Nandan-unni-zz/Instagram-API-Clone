""" API URL Configuration """

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('post/', include('post.urls')),
    path('admin/', admin.site.urls),
]
