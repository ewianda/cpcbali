from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.exceptions import ImproperlyConfigured
from django.conf.urls import patterns, include, url

from django.conf import settings
urlpatterns = patterns('',
    url('', include('facebook_access.urls')),                   
    url('', include('dictionary.urls')),
    url('', include('anthem.urls')),
    url('', include('memoire.urls')),
    url('', include('scholarship.urls')),
    url('', include('history.urls')),
    url('', include('chapters.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('users.urls')),
    url('', include('home.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('dialogos.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
       url(r'^boba-forum/', include("forum.urls")),
    url(r'^comments-thread/',        include('django_comments_xtd.urls')),
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
