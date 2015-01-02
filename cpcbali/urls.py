from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.exceptions import ImproperlyConfigured
from django.conf.urls import patterns, include, url

from django.conf import settings
urlpatterns = patterns('',
    url('', include('dictionary.urls')),
    url('', include('memoire.urls')),
    url('', include('scholarship.urls')),
    url('', include('chapters.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('users.urls')),
    url('', include('home.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments_xtd.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                            )
    try:
        urlpatterns += staticfiles_urlpatterns()
    except ImproperlyConfigured:
        pass