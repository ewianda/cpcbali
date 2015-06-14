from django.conf.urls import patterns, url
from anthem.views import AnthemDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^chapter-detail/(?P<slug>[\w-]+)/$', AnthemDetailView.as_view(), name='anthem'), 

     )
