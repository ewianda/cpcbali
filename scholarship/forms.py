from django import forms
from users.models import Boban
from scholarship.models import Scholarship
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div
from datetimewidget.widgets import DateWidget
# Create your views here.
dateTimeOptions = {
'format': 'dd/mm/yyyy HH:ii P',


}
class ScholarshipForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-7'
        self.helper.layout.append(Submit('save', 'Create scholarship'))
    
    class Meta:
        model = Scholarship
        exclude=('user',)        
        widgets = {
    #NOT Use localization and set a default format
    'deadline':DateWidget(attrs={'id':"yourdatetimeid",'format': 'dd-mm-yyyy'}, usel10n = True, bootstrap_version=3)
    }


