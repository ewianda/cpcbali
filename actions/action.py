from home.context_processors import twitterAuthenticate,FacebookAuthenticate
from django.conf import settings
from django.core.mail import send_mail
import logging

message = "BOBA dictionary has been updated. New word %s by %s. Checkout http://www.balioldboys.org/dictionary/" 
      
def socialize(modeladmin, request, queryset):
 for obj in queryset:   
     try:
         facebook  = FacebookAuthenticate()
         if obj.user:
             post = message % (obj.word,obj.user.get_full_name())
         else:
              post = message % (obj.word, "Anonymous")
         logging.error(post)     
     except:
         send_mail( subject="Trouuple with facebook",
                 message="trouble with facebook",
                 from_email=settings.EMAIL_HOST_USER,
                 recipient_list=[settings.EMAIL_HOST_USER],)
     try:
         if obj.user:
             post = message % (obj.word,obj.user.get_full_name())
         else:
              post = message % (obj.word, "Anonymous")     
         api =twitterAuthenticate()
        # api.PostUpdate(post)
         logging.error(post)
     except:
          send_mail( subject="Trouuple with twitter",
                 message="trouble with twitter",
                 from_email=settings.EMAIL_HOST_USER,
                 recipient_list=[settings.EMAIL_HOST_USER],)