from django.conf.urls import patterns, include, url
from dictionary.views import WordCreate,WordList,WordUpdate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^define-word/$', WordCreate.as_view(), name='define-word'),
	url(r'^word-definition/$', WordList.as_view(), name='word-definition'),
        url(r'^word-edit/$', WordUpdate, name='word-edit'),
     )
