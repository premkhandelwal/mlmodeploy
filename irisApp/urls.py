from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.predictor, name='predictor'),

    # path('admin/', admin.site.urls),
]
