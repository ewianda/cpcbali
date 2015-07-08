from django.conf.urls import patterns, url
from forum.views import TopicDetailView,TopicListView




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^topic-detail/(?P<slug>[-\w]+)/$',TopicDetailView.as_view(), name='topic-detail'), 
    url(r'^discussion-topics/$', TopicListView.as_view(), name='topics'),   
     )
