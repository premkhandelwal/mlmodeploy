from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('', views.predictor, name='predictor'),
    path('predict/', views.predict, name='predictor'),

    # path('admin/', admin.site.urls),
]
