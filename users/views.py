from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.shortcuts import redirect,render
from django.contrib.auth import get_user_model


from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from registration import signals
from registration.models import RegistrationProfile
from registration.backends.default.views import RegistrationView
from users.forms import UserCreationForm,SocialExtraDataForm,UserProfileForm,GeneralForm
from users.models import Boban
from django.views.generic import TemplateView
from cpcbali.decorators import render_to


from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from django.http import HttpResponse
import logging


@csrf_exempt
@login_required
def update_profile(request):  
    message = ""  
    if request.is_ajax():        
        name = request.POST.get("name",None)
        value = request.POST.get("value",None) 
        check = (hasattr(request.user, name) and (value != None))
        logging.error(value)
        logging.error(name)
        if  hasattr(request.user, name) and value:             
            usermodel =     get_user_model()
            user = usermodel.objects.get(pk = request.user.pk)            
            setattr(user,name,value)            
            user.save()            
            message = "success"    
    else:
        message = ""
        
    return HttpResponse(message)




class GeneralView(TemplateView):
       def get_context_data(self, **kwargs):
           context = super(GeneralView, self).get_context_data(**kwargs)       
           context['form'] =  GeneralForm(instance = self.request.user)
           return context
       @method_decorator(login_required)
       def dispatch(self, *args, **kwargs):
           return super(GeneralView, self).dispatch(*args, **kwargs)

class UserUpdateView(UpdateView):
    """
    Class that only allows authentic user to update their profile
    Composed of first_name,last_name,date_of_birth,gender,
    """
    model = Boban
    form_class = UserProfileForm
    template_name = "profile.html"
    success_url = "."
    def get_object(self, queryset=None):
        return self.request.user


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the events

        return context




class BobanRegistrationView(RegistrationView):
     form_class = UserCreationForm
     def register(self, request, **cleaned_data):
        """
        Given a username, email address and password, register a new
        user account, which will initially be inactive.
        Along with the new ``User`` object, a new
        ``registration.models.RegistrationProfile`` will be created,
        tied to that ``User``, containing the activation key which
        will be used for this account.
        An email will be sent to the supplied email address; this
        email should contain an activation link. The email will be
        rendered using two templates. See the documentation for
        ``RegistrationProfile.send_activation_email()`` for
        information about these templates and the contexts provided to
        them.
        After the ``User`` and ``RegistrationProfile`` are created and
        the activation email is sent, the signal
        ``registration.signals.user_registered`` will be sent, with
        the new ``User`` as the keyword argument ``user`` and the
        class of this backend as the sender.
        """
        email, password = cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(
           email, password, site,
            send_email=self.SEND_ACTIVATION_EMAIL,
            request=request,
        )
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        changed = False
        protected = ('email', 'id', 'pk')
        # Update user model attributes with the new data sent by the current
        # provider. Update on some attributes is disabled by default, for
        # example username and id fields. It's also possible to disable update
        # on fields defined in SOCIAL_AUTH_PROTECTED_FIELDS.
        for name, value in cleaned_data.items():
            
            if not hasattr(new_user, name):
                continue
            current_value = getattr(new_user, name, None)
            if not current_value or name not in protected:
                changed |= current_value != value
                setattr(new_user, name, value)
        new_user.save()
        return new_user


def context(**extra):
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)





@render_to('home.html')
def require_email(request):
    backend = request.session['partial_pipeline']['backend']
    return context(email_required=True, backend=backend)


def social_extra_data(request):
    if request.method == 'POST':
      form = SocialExtraDataForm(request.POST)
      if form.is_valid():
          request.session['profile_complete'] = True
          request.session['profile']= dict(request.POST.iteritems())
          backend = request.session['partial_pipeline']['backend']
          return redirect(reverse('social:complete', args=(backend,)),{'post':request.POST})
    else:
        form =  SocialExtraDataForm() # An unbound form

    return render(request,'home.html', {'form': form,})





