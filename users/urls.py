from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView 


from users.views import BobanRegistrationView,require_email,\
    social_extra_data,UserUpdateView,GeneralView,update_profile

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
     url(r'^general-profile/$',
             GeneralView.as_view(template_name="general.html"),
                  name='profile'),
     url(r'^social-links/$',
             TemplateView.as_view(template_name="social-links.html"),
                  name='social-links'),                  
     url(r'^mailing-list/$',
             TemplateView.as_view(template_name="mailing-list.html"),
                  name='mailing-list'), 
     url(r'^change-picture/$',
             TemplateView.as_view(template_name="picture.html"),
                  name='picture'), 
      url(r'^add-memoire/$',
             TemplateView.as_view(template_name="add-memoire.html"),
                  name='add-memoire'), 
                                                                                    
     url(r'^profile/$',update_profile, name='update-profile'),

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


