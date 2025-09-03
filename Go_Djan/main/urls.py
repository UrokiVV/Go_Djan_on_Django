# main\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newtest', views.newtest),
    path('data', views.data)
]
