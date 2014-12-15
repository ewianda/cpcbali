# Create your models here.
from __future__ import unicode_literals
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,AbstractUser

)
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _

from django.core.urlresolvers import reverse 
from PIL import Image
from datetime import date
from django_thumbs.db.models import ImageWithThumbsField


class AfricomUserManager(BaseUserManager):
      pass

def file(self, filename):
        ext = filename.split('.')[-1]
        file='{}.{}'.format(self.pk, ext)
        url = "images/users/" + file
        fullname = os.path.join(settings.MEDIA_ROOT, url)
        if os.path.exists(fullname):
            os.remove(fullname)
            ad=fullname.split('.')[0]
            dd=ad + '*'
            print ad
            os.system('rm ' +dd)
        return url

def batch(self, filename):
        ext = filename.split('.')[-1]
        file='{}.{}'.format(self.pk, ext)
        url = "images/batch/" + file
        fullname = os.path.join(settings.MEDIA_ROOT, url)
        if os.path.exists(fullname):
            os.remove(fullname)
            ad=fullname.split('.')[0]
            dd=ad + '*'
            print ad
            os.system('rm ' +dd)
        return url

HOUSE_CHOICE=(
        ('ONEIL','ONEIL'), ('SAKER','SAKER'), ('KANGSEN','KANGSEN'), ('VILLERHEUR','VILLERHEUR'),
        ('GRESS','GRESS'), ('FONYONGA','FONYONGA'), ('ASHILI','ASHILI'), ('BUNGALOW ONE','BUNGALOW TWO'),
        ('BUNGALOW ONE','BUNGALOW THREE'),('BUNGALOW ONE','BUNGALOW FOUR'),('BUNGALOW ONE','BUNGALOW FIVE'),
        ('BUNGALOW ONE','BUNGALOW SIX')
        )
ROOM_CHOICE=[('ROOM  ' + str(i), 'ROOM  ' + str(i) ) for i in range(1,27)]
YEARS=[( str(i),  str(i) ) for i in range(1,8)]
YEARS_IN_BALI = [(str(i),  str(i) ) for i in range(1954,date.today().year)]
class Boban(AbstractUser):
    nickname = models.CharField(max_length=128,verbose_name='Nickname')
    years = models.CharField(_('Years in Bali'),max_length = 32,null=True, blank = True,choices=YEARS,default="7")
    end_date = models.CharField(_('Batch of'),max_length = 32,null=True, blank = True,choices=YEARS_IN_BALI ,default="1954")
    house =  models.CharField(_('House/Bungalow'), max_length = 32, blank = True,choices=HOUSE_CHOICE,default="ONEIL")
    room =  models.CharField(_('Dorm/Room'), max_length = 32, blank = True,choices=ROOM_CHOICE,default="ROOM 1")
    memoir=  models.CharField(_('Fun memories'), max_length = 255, blank = True)
    country = models.CharField(_('Country'), max_length = 100, blank = True)
    city = models.CharField(_('City'), max_length = 100, blank = True)
    picture =  ImageWithThumbsField(upload_to=file, blank = True, sizes=((125,125),(200,200)))
    notification = models.BooleanField(_('Receive info about Boba events'),default=True)
    activation_key = models.CharField(null=True,max_length=40)
    key_expires = models.DateTimeField(null=True)	
    def get_absolute_url(self): 
       return reverse('user_detail', kwargs={'pk': self.pk})

       """ def save(self, size=(400, 300), *args, **kwargs):
       
        Save Photo after ensuring it is not blank.  Resize as needed.
        
        if not self.id and not self.picture:
            return		
        super(Boban, self).save(*args, **kwargs)
        
        filename = self.picture
        image = Image.open(filename)    
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename.path)
		super(Boban, self).save(*args, **kwargs) """
		
Boban._meta.get_field('email')._unique = True  

class Batch(models.Model):
    picture =  ImageWithThumbsField(upload_to=batch, blank = True, sizes=((125,125),(200,200)))
    end_date = models.CharField(_('Batch of'),max_length = 32,null=True, blank = True,choices=YEARS_IN_BALI ,default="1954")
    def __unicode__(self):
	 return self.end_date
    def get_absolute_url(self):
        return reverse('batch')

