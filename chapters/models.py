from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django_thumbs.db.models import ImageWithThumbsField
import os
from django.utils.translation import ugettext_lazy as _
# Create your models here.

def file(self, filename):
        ext = filename.split('.')[-1]
        file='{}.{}'.format(self.pk, ext)
        url = "images/chapter/cover/" + file
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
        url = "images/chapter/logo/" + file
        fullname = os.path.join(settings.MEDIA_ROOT, url)
        if os.path.exists(fullname):
            os.remove(fullname)
            ad=fullname.split('.')[0]
            dd=ad + '*'
            print ad
            os.system('rm ' +dd)
        return url
from django.utils import timezone
class Chapter(models.Model):
    name = models.CharField(_('Chapter Name'),max_length=30,unique=True)
    location= models.CharField(max_length=200, blank = True)
    description= RichTextField()
    logo =  ImageWithThumbsField(upload_to=batch, blank = True, sizes=((125,125),(200,200)))
    cover =  ImageWithThumbsField(upload_to=file, blank = True, sizes=((125,125),(200,200)))
    creation_date = models.DateTimeField(_('Date Created'), default=timezone.now)
    approved = models.BooleanField(_('Approval'), default=False)
    creator= models.ForeignKey(settings.AUTH_USER_MODEL,related_name='chapter_creator')
    def __unicode__(self):
     return self.name