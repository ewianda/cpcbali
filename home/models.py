from django.db import models

from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _



class History(models.Model):
  name =  models.CharField(max_length=30)
  history =  RichTextField(_('title'), max_length = 255, blank = True)
  
  def __unicode__(self):
	 return self.name
  def css_id(self):
      return self.name.replace(" ", "")
