from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator

from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from users.models import Boban,Batch
from django.views.generic.detail import DetailView
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div
from django.core.urlresolvers import reverse
import datetime, random, sha, json
from django.views.generic.edit import CreateView
 
from users.admin import UserChangeForm
from users.forms import  CustomUserCreationForm,UserForm
@csrf_exempt
def login_user(request):
     message="Your email and password didn't match. Please try again"
     redirect_to = request.POST.get('next', '/')     
     if request.is_ajax():
        form =  AuthenticationForm(data=request.POST)
        if form.is_valid():
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=username, password=password)
           if user is not None:
                 login(request, user)
                 print redirect_to
                 return HttpResponse(json.dumps({'message': ''}),content_type='application/json')
        else:
                 
                 return HttpResponse(json.dumps({'message': message}),content_type='application/json')
     return HttpResponse(json.dumps({'message': ''}))


@csrf_exempt
def ajax_check_auth(request):
    respond = False
    if request.is_ajax():
        if request.user.is_authenticated():
            respond = True
    mimetype = 'application/json'    
    return HttpResponse(respond)

class UserCreateView(CreateView):
    model = Boban
    form_class =CustomUserCreationForm
    template_name = 'users/registration_form.html'
    success_url = '/'
    
    def get_form_kwargs(self):
       kwargs = {'initial': self.get_initial()}
       if self.request.method in ('POST', 'PUT'):
         username = self.request.POST.get('email') 
         self.request.POST['username'] = username
         kwargs.update({
            'data': self.request.POST,
            'files': self.request.FILES,
             })
       return kwargs        

@login_required
def userprofile(request):
    user = get_user_model()
    profile = user.objects.get(pk=request.user.id)
    
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        form = UserChangeForm(instance=profile)
    return render(request,"users/profile.html", {
        "form": form,
    })

        
class UserUpdateView(UpdateView):
    model = Boban
    form_class=UserForm
    template_name = 'users/profile.html'      
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)
    
class UserDetailView(DetailView):
    """
    Class to display user profile in detail
    """
    model = Boban
    template_name = "users/user_detail.html"  
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDetailView, self).dispatch(*args, **kwargs)

class ActivationView(TemplateView):
    template_name = "users/activate.html"
    success_url ="/"
    def get_context_data(self, **kwargs):
        activation_key = kwargs.get('activation_key')
	try:
             account  = Boban.objects.get(activation_key=activation_key)
        except Boban.DoesNotExist:
             account = None
        context = super(ActivationView, self).get_context_data(**kwargs)
        if account:
           if account.is_active:
              context['active']="active"
           else:
               account.is_active = True	
               account.save()
               context['success'] = "success"			   
        return context

