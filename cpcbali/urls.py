from django.contrib import admin
admin.autodiscover()

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',
    url('', include('dictionary.urls')),
    url('', include('memoire.urls')),
    url('', include('scholarship.urls')),
    url('', include('users.urls')),
    url('', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^comments/', include('django_comments_xtd.urls'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
