from django.contrib import admin
from django.urls import path, include
from blog import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('', include('web_site.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    