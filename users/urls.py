from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from users.views import UserUpdateView,UserDetailView,UserCreateView,ActivationView
from users import views
urlpatterns = patterns('',
    url(r'^update-profile/(?P<pk>\d+)/$',UserUpdateView.as_view(), name='update-profile'),
    url(r'^ajax_check_auth/', views.ajax_check_auth, name='ajax'),
    url(r'^profile/$', 'users.views.userprofile', name='profile'),
    url(r"^my-profile/(?P<pk>\d+)/$", UserDetailView.as_view(), name="user_detail"),
    url(r"^create-account/$", UserCreateView.as_view(), name="register"),
    url(r'^activate/(?P<activation_key>\w+)/$',ActivationView.as_view(),name='registration_activate'),
    url(r'^logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r"^accounts/login/$", views.login_user, name = "login"),
)

        
