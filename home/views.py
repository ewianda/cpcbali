from django.shortcuts import render
from home.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from users.models import Boban,Batch
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView


from home.models import Achievement


class AchievementListView(ListView):
      model = Achievement
      
      
def home(request):   
   user = get_user_model()
   myuser = user.objects.filter(is_active=True)
   return render(request,'home/index.html',{'myuser':myuser})

def contact_form(request):
   form = ContactForm()
   if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "{name} / {email} said: ".format(
                  name=form.cleaned_data.get('name'),
                  email=form.cleaned_data.get('email'))
            message += "\n\n{0}".format(form.cleaned_data.get('message'))
            send_mail(
                 subject=form.cleaned_data.get('subject').strip(),
                 message=message,
                 from_email='contact-form@myapp.com',
                 recipient_list=[settings.EMAIL_HOST_USER],)
            return render(request,"home/contact.html", {"form":form,"message": "message was sent",})
   return render(request,"home/contact.html", {"form": form,})


def batch_view(request,class_of):     
       user = get_user_model()
       try:       
         profile = user.objects.all().filter(end_date=str(class_of))
       except user.DoesNotExist:
           profile = None
       try:             
          batch = Batch.objects.get(end_date=str(class_of))
       except Batch.DoesNotExist:
            batch=None          
       return render(request,"home/class_off.html", {"profile":profile,"batch":batch,})
       

