from django.shortcuts import render
from django.views.generic.edit import CreateView
from chapters.models import Chapter
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div
# Create your views here.


# Create your views here.
class ChapterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChapterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout.append(Submit('save', 'Add definition'))

    class Meta:
        model = Chapter
        exclude=('approved','creator','creation_date',)
        widgets = {
            'definition': Textarea(attrs={'cols': 8, 'rows': 10}),
        }

class CreateChapter(CreateView):
    model = Chapter
    form_class = ChapterForm
    success_url = '/new-chapter/'
    paginate_by = 8  #and that's it !!
   # template_name = "dictionary/define-word.html"
    template_name = "chapters/index.html"
    def get_context_data(self, **kwargs):
        words = self.model.objects.all()        
        kwargs['object_list'] = words.order_by('name')
        return super(CreateChapter, self).get_context_data(**kwargs)
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(CreateChapter, self).form_valid(form)
    
    