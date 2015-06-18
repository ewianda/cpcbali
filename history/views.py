from django.shortcuts import render
from history.models import  History,Principal,PrincipalBiography
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.utils import timezone
from history.forms import PrincipalUpdateForm
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
# Create your views here.
class HistoryDetailView(DetailView):
    model = History
    def get_context_data(self, **kwargs):
        context = super(HistoryDetailView, self).get_context_data(**kwargs)
        context['history_list'] = History.objects.all()
        return context
    
    
class PrincipalDetailView(DetailView):  
    model = Principal
    def get_context_data(self, **kwargs):
        context = super(PrincipalDetailView, self).get_context_data(**kwargs)
        context['object_list'] = Principal.objects.all()
        return context
    
    
class PrincipalUpdateView(UpdateView):
      model =Principal        
      form_class=    PrincipalUpdateForm  
      def get_initial(self):
          return {"biography":self.object.biography()}
      def get_success_url(self):
         return reverse('thanks')  
      def form_valid(self, form):
          bio=PrincipalBiography(principal=self.object,biography=form.cleaned_data.get('biography'))          
          if self.request.user.is_authenticated():  
             bio.user = self.request.user           
        #self.object.save()
          bio.save()           
          send_mail( subject="New word added",
               message="%s:%s" % (self.object.name,bio),
               from_email=settings.EMAIL_HOST_USER,
               recipient_list=[settings.EMAIL_HOST_USER],)          
          return super(PrincipalUpdateView, self).form_valid(form) 
    
    
class PrincipalListView(ListView):
    model = Principal 
    def get_context_data(self, **kwargs):
        context = super(PrincipalListView, self).get_context_data(**kwargs)
        context['history_list'] = History.objects.all()
        return context 