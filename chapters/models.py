from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django_thumbs.db.models import ImageWithThumbsField
import os
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

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
    
    

class Chapter(models.Model):
    name = models.CharField(_('Chapter Name'),max_length=30,unique=True)
    location= models.CharField(max_length=200)
    description= RichTextField()
   
    cover =  models.ImageField(upload_to=file,null=True, blank = True )
    creation_date = models.DateTimeField(_('Date Created'), default=timezone.now)
    approved = models.BooleanField(_('Approval'), default=False)
    slug = models.SlugField(null=True, blank=True) 
    facebook = models.URLField(help_text=_('e.g.https://www.facebook.com/profile.php?id=501348704'),blank=True, null=True)
    twitter = models.URLField(help_text=_('e.g. https://plus.google.com/107176605982323643354/posts'),blank=True, null=True)
    google_plus = models.URLField(help_text=_('e.g.https://twitter.com/WiandaElvis'),blank=True, null=True)
    
    def __unicode__(self):
        return self.name
   
    
    def get_absolute_url(self):
        return reverse('chapter-detail', kwargs={'slug': self.slug})
    def users(self):
        return self.chapter_member.all()
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.name)
        super(Chapter, self).save(*args, **kwargs)
        
        
class ChapterMember(models.Model):
    member = models.ForeignKey(User,unique=True)
    chapter = models.ForeignKey(Chapter,related_name='chapter_member')  
          
    
    
    
    
    