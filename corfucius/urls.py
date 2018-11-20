from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  #this links to the urls.py of the pages app
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
