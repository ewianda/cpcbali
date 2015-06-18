from django.conf.urls import patterns, url
from chapters.views import CreateChapter,ChapterDetailView,ChapterListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPCbali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create-chapter/$', CreateChapter.as_view(), name='create-chapter'),
    url(r'^chapter-detail/(?P<slug>[\w-]+)/$', ChapterDetailView.as_view(), name='chapter-detail'), 
    url(r'^chapter-list$', ChapterListView.as_view(), name='chapter'),   
     )
