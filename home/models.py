from django.db import models

from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _



class History(models.Model):
  history =  RichTextField(_('Fun memories'), max_length = 255, blank = True)
  def __unicode__(self):
	 return "HISTORY"
