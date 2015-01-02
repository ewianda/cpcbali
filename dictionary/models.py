from django.db import models
from django.conf import settings
# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=30)
    definition= models.CharField(max_length=200)
    vote = models.IntegerField(default=0,blank = True)
    user= models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
	 return self.word
        
