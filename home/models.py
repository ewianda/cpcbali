from django.db import models

from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

class Achievement(models.Model):  
    name =  models.CharField(max_length=30)
    description =  RichTextField( max_length = 255, blank = True)
    image = models.ImageField(upload_to='achievement')
    def __unicode__(self):
     return self.name