from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div

from history.models import  History,Principal

class PrincipalUpdateForm(forms.ModelForm):   
    biography = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(PrincipalUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout.append(Submit('save', 'Add Biography'))   
    
    
    class Meta:
        model = Principal
        fields =['biography',]
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 8, 'rows': 10}),
        }