from django.conf.urls import patterns, include, url
from users.views import BobanRegistrationView,require_email,social_extra_data,UserUpdateView

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Overide the Registration URL in registration.backends.default
     url(r'^profile/$',UserUpdateView.as_view(), name='profile'),

     url(r'^email/$', require_email, name='require_email'),
     url(r'^complete_information/$', social_extra_data, name='social_extra_data'),

    url(r'^accounts/register/$',
                          BobanRegistrationView.as_view(),
                           name='registration_register'),
    url(r'^login/',
        'django.contrib.auth.views.login',
        name='login'),
     url(r'^accounts/',
        include('registration.backends.default.urls')),

     )


