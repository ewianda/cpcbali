from captcha.fields import ReCaptchaField  # Only import different from yesterday
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Div
from crispy_forms.bootstrap import PrependedText
from django import forms

SUBJECT=(('Suggestions','Suggestions'),('Web Developement','Web Developement'),('Adding information','Adding information'))
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.ChoiceField(widget=forms.Select,choices=SUBJECT,required=True)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(label='Please enter exact text',)  # Only field different from yesterday

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'well col-xs-12 row'
        self.helper.layout = Layout(
                Div(
                    'name',
                    PrependedText('email','<span class="glyphicon glyphicon-envelope"></span>'),
                    'subject',
                    'captcha',
                    css_class = 'col-xs-4'
                    ),   
                Div(   'message',
                    css_class = 'col-xs-8'
                    )
                )
        self.helper.layout.append(Div(Submit('submit', 'Submit',css_class="btn-success pull-right")) )       
        super(ContactForm, self).__init__(*args, **kwargs)
