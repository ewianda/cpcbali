from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from dictionary.models import Word
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div
from home.context_processors import twitterAuthenticate
# Create your views here.
class WordForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout.append(Submit('save', 'Add definition'))
    
    
    def clean_word(self):      
        return self.cleaned_data['word'].capitalize()
    
    class Meta:
        model = Word
        exclude=('vote','user')
        widgets = {
            'definition': Textarea(attrs={'cols': 8, 'rows': 10}),
        }

class WordList(ListView):
    model = Word
    paginate_by = 8  #and that's it !!
   # template_name = "dictionary/define-word.html"
   # template_name = "dictionary/word_list.html"
    def get_context_data(self, **kwargs):
        words = self.model.objects.all()        
        kwargs['objet_list'] = words.order_by('word')
        return super( WordList, self).get_context_data(**kwargs)
		
	
class WordCreate(CreateView):
    form_class = WordForm
    
    model = Word    
    def get_success_url(self):
         return reverse('dictionary')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        try:
            api =twitterAuthenticate()
            message = "%s has added a new word , %s to BOBA dictionary. Checkout http://www.balioldboys.org/dictionary/" % (self.request.user.full_name , self.object.word)
            api.PostUpdate(message)
        except:
            pass
        return super(WordCreate, self).form_valid(form)    
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WordCreate, self).dispatch(*args, **kwargs)


def WordUpdate(request):    
    respond = False
    if request.is_ajax():
        pk = request.POST.get('pk', '')
        value = request.POST.get('value', '')
        word = Word.objects.get(pk=pk)
        if value:
             word.definition = value
             word.save()
        if request.user.is_authenticated():
            respond = True
            print respond
    mimetype = 'application/json'    
    return HttpResponse(respond)
     
