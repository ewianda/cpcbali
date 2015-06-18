from django.conf.urls import patterns, url
from scholarship.views import ScholarshipCreateView, ScholarshipDetailView,ScholarshipListView




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^scholarship-detail/(?P<pk>\d+)/$',ScholarshipDetailView.as_view(), name='scholarship-detail'), 
    url(r'^scholarship-list/$', ScholarshipListView.as_view(), name='scholarship'),   
    url(r'^start-a-scholarship/$', ScholarshipCreateView.as_view(), name='scholarship-create'),
     )
