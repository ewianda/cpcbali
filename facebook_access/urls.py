from facebook_access import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',                       
   url(r'^facebook-access-tooken/$',   views.get_facebook_access_token,name="facebook-access")  ,  
   
   )                