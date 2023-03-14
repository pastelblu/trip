from django.urls import path
from . import views, admin

urlpatterns = [

    path('', views.demo, name='demo'),
]