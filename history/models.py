from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
import datetime
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
    class Meta:
        ordering = ['from_date'] 
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
 
from django.utils.dates import MONTHS
import datetime
YEAR_CHOICES = []
for r in range(1949, (datetime.datetime.now().year)):
    YEAR_CHOICES.append((r,r))  
    
DAY_CHOICES = []
for r in range(1, (32)):
    DAY_CHOICES.append((r,r))     
       
class TimeLog(models.Model):
    year =  models.IntegerField(_('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month = models.PositiveSmallIntegerField(choices=MONTHS.items(),blank = True, null = True)
    day = models.IntegerField(_('Day'), max_length=2, choices=DAY_CHOICES,blank = True, null = True)
  
    event = RichTextField(_('event'), max_length = 255)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank = True, null = True) 
    def __unicode__(self):
        return str(self.year)    
    class Meta:
        ordering = ['year']   
    def new_month(self):
        if not self.get_month_display():
            return '' 
        else:
            return self.get_month_display()
    def new_day(self):
        if not self.day:
            return '' 
        else:
            return self.day
        
        
       