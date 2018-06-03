from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^about-us/', include('about.urls')),
    url(r'^production/', include('production.urls')),
    url(r'^contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
