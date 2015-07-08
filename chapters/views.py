from django.views.generic.edit import CreateView
from chapters.models import Chapter
from users.models import Boban
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from chapters.form import  ChapterFormSet,ChapterForm,ChapgerFormSetHelper
# Create your views here.
class ChapterDetailView(DetailView):
    model = Chapter
      
    
    
class ChapterListView(ListView):
    model = Chapter 
    def get_context_data(self, **kwargs):
        context = super(ChapterListView, self).get_context_data(**kwargs)        
        context['national_chapter'] = self.model.objects.get(slug='national-chapter')
        context['users'] = Boban.objects.all()
        return context 


class CreateChapter(CreateView):
    model = Chapter
    form_class = ChapterForm
    #success_url = '/new-chapter/'
    paginate_by = 8  #and that's it !!
    #template_name = "dictionary/define-word.html"
    #template_name = "chapters/index.html"
    def get_context_data(self, **kwargs):
        context = super(CreateChapter, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ChapterFormSet(self.request.POST)
            context['helper'] =ChapgerFormSetHelper()
        else:
            context['formset'] = ChapterFormSet()
            context['helper'] =ChapgerFormSetHelper()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            form.instance.creator = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super(CreateChapter, self).form_valid(form)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateChapter, self).dispatch(*args, **kwargs)
    
    