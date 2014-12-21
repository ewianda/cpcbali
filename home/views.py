from django.shortcuts import render
from home.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from users.models import Boban,Batch
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.utils import timezone

from home.models import History

class HistoryListView(ListView):
      model = History


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


def batch_view(request):
   batch=Batch.objects.get(pk=1)
   if request.method == 'GET':
       class_of = request.GET.get('class_of', 2003)
       user = get_user_model()
       print class_of
       if class_of:
           profile = user.objects.filter(end_date__contains=str(class_of))
           for p in profile:
               print p.nickname
           return render(request,"home/class_off.html", {"profile":profile,"batch":batch,'next': reverse('comments-xtd-sent')})
       else:
           return render(request,"home/class_off.html", {"batch":batch,'next': reverse('comments-xtd-sent')})
   else:
       return render(request,"home/class_off.html", {"batch":batch,'next': reverse('comments-xtd-sent')})


