from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve


STATIC_URL = settings.STATIC_URL

if STATIC_URL.startswith('/'):
    STATIC_URL = STATIC_URL[1:]


urlpatterns = [
    url(r'^xqueue/', include('queue.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^{}/(?P<path>.*)$'.format(STATIC_URL), serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]
