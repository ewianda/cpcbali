from django.contrib.auth.forms import UserCreationForm
from users.models import Boban
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div
import datetime, random, sha, json


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Boban
	fields=('username','first_name','email',
                'last_name', 
                'country',
                'city','picture','nickname','years','end_date',
		'memoir',
                'house',
                'room','notification')
        widgets = {
            'memoir': forms.Textarea(attrs={'cols': 56, 'rows': 6}),
        }
       # ('nickname', 'email')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Boban.objects.get(username=username)
        except Boban.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
        """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(label='Username',widget = forms.HiddenInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-7'
        self.helper.layout = Layout(
               Div(Div(Fieldset(
                'Account Information',
                'email',
                'first_name',
                'last_name', 
                'password1',
                'password2'),css_class='fieldset col-sm-6'
                 ),
                Div(Fieldset(
                'Personal Information',
                'country',
                'city','picture','notification'),css_class=' col-sm-6 fieldset'               
                 ),css_class='row' )                
                    )
    
        self.helper.layout.append(Div(Fieldset(
                   'When I was in CPC',
                   Div(
                   'nickname','years','end_date'		   
                      ,css_class='col-sm-6 fieldset'),
                   Div('house','room',css_class='col-sm-6 fieldset')
                   ),css_class='row fieldset'))				   
        self.helper.layout.append(Div(Fieldset(
                   'Memoire','memoir'
                   ),css_class='row fieldset'))
        self.helper.layout.append(Submit('save', 'Submit form'))
		
     
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print self.cleaned_data
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

         
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        salt = sha.new(str(random.random())).hexdigest()[:5]
        user.is_active=False
        user.activation_key = sha.new(salt+user.email).hexdigest()
        user.key_expires = datetime.datetime.today() + datetime.timedelta(2)
        from django.core.mail import send_mail
        print "I got here to save the form"
        email_subject = 'Your new Boban account confirmation'
        email_body ="Hi Bob %s and thanks for being part of our new Boban webisite \n activate nour account at http://camprocol.ddns.net:8000/activate/%s"  % (user.first_name,user.activation_key)
        send_mail(email_subject,
                      email_body,
                      'wiandaelvis@gmail.com',
                      [user.email])

        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(                
                Fieldset(
                'Personal Information', 
                'country',
                'city','picture'               
                 )                
                    )    
        self.helper.layout.append(Fieldset(
                'When I was in CPC',
		'memoir',
                'nickname',
                'house',
                'room'))
        self.helper.layout.append(Fieldset( 
                'Receive notifications about Boban meetings and activities in your area',
                'notification'
                            )
                )



        self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-3'


    class Meta:
        model = Boban
        fields  = ('memoir','country','city','picture','nickname','house','room','notification',)
        widgets = {
            'memoir': forms.Textarea(attrs={'cols': 5, 'rows': 10}),
        }


