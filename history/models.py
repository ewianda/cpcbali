from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class History(models.Model):
    name =  models.CharField(max_length=30)
    history =  RichTextField(_('title'), max_length = 255, blank = True)
    slug = models.SlugField(max_length=100,unique=True)
    def __unicode__(self):
        return self.name
    def css_id(self):
        return self.name.replace(" ", "")
    @models.permalink
    def get_absolute_url(self):
        return ('history', (),{'slug': self.slug})

class Principal(models.Model):
    name =  models.CharField(max_length=30)    
    image = models.ImageField(upload_to='principal')
    slug = models.SlugField(max_length=100,unique=True)
    from_date = models.DateField()
    to_date = models.DateField()
    
    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('principal-detail', (),{'slug': self.slug})
    def get_update_url(self):
        return reverse('principal-update', kwargs={'slug': self.slug})     
    
    def biography(self):
        try:
            return self.biographies.filter(approved=True)[0].biography
        except:
            return None
        
class PrincipalBiography(models.Model): 
        biography =  RichTextField(_('biography'), max_length = 255)
        principal = models.ForeignKey(Principal,related_name='biographies')
        user = models.ForeignKey(settings.AUTH_USER_MODEL,blank = True, null = True)
        approved = models.BooleanField(default=False)
        
     
        
        
        
        
       