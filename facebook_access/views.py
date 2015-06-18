from django.shortcuts import render
import datetime
# Create your views here.
from open_facebook import OpenFacebook,FacebookAuthorization
from django.core.urlresolvers import reverse
from facebook_access.models import FaceBookAcessToken

def get_facebook_access_token(request):
    me = []
    if request.method == 'GET':
        code = request.GET.get('code',None)
        redirect_uri = "http://localhost:8000%s"  % reverse('facebook-access')      
        
        response=FacebookAuthorization.convert_code(code,redirect_uri =redirect_uri)
        
        access_token=response.get('access_token',None)
        expire  = response.get('expires',None)
        expiration = datetime.datetime.now() + datetime.timedelta(seconds=int(expire))
        try:
            stored_token = FaceBookAcessToken.objects.all()[0]
            stored_token.access_token=access_token
            stored_token.expiration=expiration
        except:
             stored_token = FaceBookAcessToken(access_token=access_token,expiration=expiration)
        stored_token.save()    
        facebook=OpenFacebook(access_token)
        me =facebook.get('me')
    return render(request,"facebook_access/facebook_access.html", {"me":me,})