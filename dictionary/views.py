from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect,HttpResponse,Http404

from dictionary.models import Word
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div

# Create your views here.
class WordForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout.append(Submit('save', 'Add definition'))

    class Meta:
        model = Word
        exclude=('vote','user')
        widgets = {
            'definition': Textarea(attrs={'cols': 8, 'rows': 10}),
        }

class WordCreate(CreateView):
    model = Word
    form_class = WordForm
    success_url = '/define-word/'
    template_name = "dictionary/define-word.html"
    def get_context_data(self, **kwargs):
        words = self.model.objects.all()
        wd = self.request.GET.get('word')
        print wd
        if wd:
            words = words.filter(word__startswith=wd)
        kwargs['object_list'] = words.order_by('word')
        return super(WordCreate, self).get_context_data(**kwargs)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WordCreate, self).form_valid(form)
		
	
class WordList(ListView):
    model = Word
    template_name = "dictionary/word-definition.html"


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
     
