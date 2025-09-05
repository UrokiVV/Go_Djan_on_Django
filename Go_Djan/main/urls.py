# main\urls.py
from django.urls import path
from . import views

urlpatterns = [
    # DJ02
    path('', views.index, name='index'),
    path('newtest', views.newtest, name='newtest'),
    path('data', views.data, name='data'),
    path('next04', views.next04, name='next04'),
    path('about', views.about, name='about'), # footer
    # DJ01
    path('index01', views.index01),
    path('new', views.new),
    path('newtest01', views.newtest01),
    path('data01', views.data01)
]
