from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div,HTML,Field
from ckeditor.widgets import CKEditorWidget
from history.models import  History,Principal,TimeLog
from captcha.fields import ReCaptchaField 
import datetime


 
class TimeLogForm(forms.ModelForm):   
    captcha = ReCaptchaField(label='Please enter exact text',) 
    #time = forms.CharField()  
    def __init__(self, *args, **kwargs):
        super( TimeLogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
                                    Field(HTML('<span>'),Field('day'),'month','year',HTML('<span>')),
                                    
                                    'event')
        self.helper.layout.append(Submit('save', 'Add Time Line'))    
        
    class Meta:
        model = TimeLog
        fields =['day','month','year','event',]
        widgets = {
            'event': forms.Textarea(attrs={'cols': 8, 'rows': 10}),
        }
    def clean(self):
           self.cleaned_data = super(TimeLogForm, self).clean()        
           day = self.cleaned_data.get('day')
           month = self.cleaned_data.get('month')
           year = self.cleaned_data.get('year')
           try:
               newDate = datetime.datetime(year,month,day)
           except:
                raise forms.ValidationError("Day selected is out of month range")             
           return self.cleaned_data
            
class PrincipalUpdateForm(forms.ModelForm):   
    biography = forms.CharField(widget=CKEditorWidget())
    captcha = ReCaptchaField(label='Please enter exact text',)
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