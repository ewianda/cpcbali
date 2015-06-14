from django.conf.urls import patterns, include, url
from history import views


urlpatterns = patterns('',
        #url(r'^$',RedirectView.as_view(url=reverse_lazy('history-list',kwargs={'slug':'history'})),
        #name='history'),            
        url(r'^history/(?P<slug>[\w-]+)/$', views.HistoryDetailView.as_view(),name="history"),        
        url(r'^principals/$', views.PrincipalListView.as_view(),name="principals"),
        url(r'^principal/(?P<slug>[\w-]+)/$', views.PrincipalDetailView.as_view(), name='principal-detail'), 
        )