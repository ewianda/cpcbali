from django.shortcuts import render
from history.models import  History,Principal,PrincipalBiography,TimeLog
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView
from django.utils import timezone
from history.forms import PrincipalUpdateForm,TimeLogForm 
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
          send_mail( subject="Principal Bio added",
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
    

class TimeLogListView(ListView):
    model = TimeLog    
    def get_queryset(self):
        return self.model.objects.filter(approved=True)
class TimeLogCreateView(CreateView):
    form_class=    TimeLogForm 
    model = TimeLog  
    def get_success_url(self):
         return reverse('thanks')
    def form_valid(self, form):  
        self.object = form.save(commit=False)
        if self.request.user.is_authenticated():  
             self.object.user = self.request.user
             self.object.approved = False
             send_mail( subject="Time line added",
                 message="%s:%s" % (self.object.event,self.object.user),
                 from_email=settings.EMAIL_HOST_USER,
                 recipient_list=[settings.EMAIL_HOST_USER],)
             #self.object.save()
             #send_mail( subject="New timelog added",
              # message="%s:%s" % (str(self.object.time),self.object.event),
              # from_email=settings.EMAIL_HOST_USER,
              # recipient_list=[settings.EMAIL_HOST_USER],)          
        return super(TimeLogCreateView, self).form_valid(form) 
    