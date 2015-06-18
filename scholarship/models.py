from django.db import models
from users.models import Boban
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
# Create your models here.
class Scholarship(models.Model):
    name = models.CharField(_('Name of Scholarship'),max_length=30,unique=True)
    deadline = models.DateField(auto_now_add=True)
    requirement =  RichTextField(blank=True, null=True)
    user= models.ForeignKey(Boban)
    def get_absolute_url(self):
        return reverse('scholarship-detail', kwargs={'pk': self.pk})
    
    
    def __unicode__(self):
	    return self.name
       
       
