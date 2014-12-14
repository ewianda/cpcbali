from django.conf.urls import patterns, include, url
from scholarship.views import ScholarshipCreateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^scholarship/$', ScholarshipCreateView.as_view(), name='scholarship'),

     )
