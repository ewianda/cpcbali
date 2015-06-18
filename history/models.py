from django.db import models

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


class Principal(models.Model):
  name =  models.CharField(max_length=30)
  bio =  RichTextField(_('title'), max_length = 255, blank = True)
  image = models.ImageField(upload_to='principal')
  slug = models.SlugField(max_length=100,unique=True)
  def __unicode__(self):
     return self.name
