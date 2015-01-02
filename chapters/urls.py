from django.conf.urls import patterns, include, url
from chapters.views import CreateChapter

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^new-chapter/$', CreateChapter.as_view(), name='chapter'),   
     )
