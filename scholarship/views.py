from scholarship.forms import ScholarshipForm
from django.views.generic.edit import CreateView
from scholarship.models import Scholarship
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ScholarshipDetailView(DetailView):
    model =Scholarship 
      
    
    
class ScholarshipListView(ListView):
    model = Scholarship 

class ScholarshipCreateView(CreateView):
    #template_name = 'scholarship/scholarship.html'
    model = Scholarship
    #success_url = '/'
    form_class =ScholarshipForm
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ScholarshipCreateView, self).form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super( ScholarshipCreateView, self).dispatch(*args, **kwargs)