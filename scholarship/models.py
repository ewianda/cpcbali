from django.db import models
from users.models import Boban
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Scholarship(models.Model):
    name = models.CharField(_('Name of Scholarship'),max_length=30)
    deadline = models.DateField()
    requirement = models.TextField(max_length=30)    
    user= models.ForeignKey(Boban)
    def __unicode__(self):
	 return self.name
