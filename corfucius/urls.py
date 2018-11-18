
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  #this links to the urls.py of the pages app
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
