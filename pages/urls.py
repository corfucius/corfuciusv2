#need to import path in order to define paths
from django.urls import path
#import views for views.py methods
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('gallery', views.gallery, name='gallery')
]