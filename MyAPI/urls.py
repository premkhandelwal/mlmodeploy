
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('user', views.user,  name='user')
]
