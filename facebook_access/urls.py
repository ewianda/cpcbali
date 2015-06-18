from django.conf.urls import patterns, url
from facebook_access.views import get_facebook_access_token 




urlpatterns = patterns('',

    url(r'^get-facebook-access-token/$',get_facebook_access_token, name='facebook-access'),   
     )
