from users.models import Boban
from django import forms
from chapters.models import Chapter,ChapterMember
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div
from django.forms.models import inlineformset_factory
# Create your views here.
class ChapgerFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ChapgerFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag=False        
        self.render_required_fields = True,




class ChapterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChapterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.form_tag=False
        #self.helper.layout.append(Submit('save', 'Add definition'))

    class Meta:
        model = Chapter
        exclude=('approved','creator','creation_date','slug')
        widgets = {
            'definition': Textarea(attrs={'cols': 8, 'rows': 10}),
        }

ChapterFormSet = inlineformset_factory(Chapter, ChapterMember,\
                                       can_delete=False,max_num=9,extra=9)









