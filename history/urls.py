from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from history import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
        #url(r'^$',RedirectView.as_view(url=reverse_lazy('history-list',kwargs={'slug':'history'})),
        #name='history'),            
        url(r'^history/(?P<slug>[\w-]+)/$', views.HistoryDetailView.as_view(),name="history"),        
        url(r'^principals/$', views.PrincipalListView.as_view(),name="principals"),

        )