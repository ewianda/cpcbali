from django.conf.urls import patterns, include, url
from dictionary.views import WordCreate,WordList,WordUpdate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add-word/$', WordCreate.as_view(), name='add-word'),
	url(r'^dictionary/$', WordList.as_view(), name='dictionary'),
    url(r'^edit-word/$', WordUpdate, name='edit-word'),
     )
