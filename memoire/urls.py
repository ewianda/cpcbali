from django.conf.urls import patterns, include, url
from memoire.views import MemoireList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^memoire/$', MemoireList.as_view(), name='memoire'),
)
