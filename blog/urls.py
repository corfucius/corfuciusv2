 
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='blog'),
    #path('details/(<id>\d+)/$', views.details, name='details'),
    path('details/<int:blog_id>', views.details, name='details'),
]
