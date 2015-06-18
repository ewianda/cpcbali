from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter

from open_facebook import OpenFacebook,FacebookAuthorization


def FacebookAuthenticate():  
    FACEBOOK_ACCESS_TOKEN= FacebookAuthorization.get_app_access_token()

    return  OpenFacebook(FACEBOOK_ACCESS_TOKEN)
    


def latest_posts( request ):  
    posts = cache.get('posts')
    if posts: 
        return {"posts": posts}
    posts=[]
    try:
        facebook  = FacebookAuthenticate()
        
        feed=facebook.get(settings.FACEBOOK_GROUP_FEED)['data']
    except:
        feed = None
        
    if feed:   
        for x in range(1):
            posts.append(feed[x]['actions'][0]['link'])  
        cache.set( 'posts', posts, settings.TWITTER_TIMEOUT )    
        return {"posts": posts}
    else:
        return {"posts": []}
   
   

def twitterAuthenticate():  
    consumer_key=settings.SOCIAL_AUTH_TWITTER_KEY
    consumer_secret=settings.SOCIAL_AUTH_TWITTER_SECRET
    access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY
    access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET     
    api = twitter.Api(consumer_key= consumer_key,consumer_secret= consumer_secret,\
                      access_token_key= access_token_key,\
                      access_token_secret= access_token_secret,cache=None)
    return api 
      


def latest_tweets( request ):
    tweets = cache.get('tweets')
    if tweets:
       return {"tweets": tweets}
    tweets=[]
    api = twitterAuthenticate()
   
    status=api.GetUserTimeline( settings.TWITTER_USER )[:2]
    for x in range(1):
        tweets.append({"id":status[x].id,"user":status[x].user.screen_name})     
    cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )
    return {"tweets": tweets}





