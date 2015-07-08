from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=30,unique=True)   
    user= models.ForeignKey(settings.AUTH_USER_MODEL,blank = True, null = True)
    slug = models.SlugField(null=True, blank=True) 
    def __unicode__(self):
	    return self.word
    class Meta:
        ordering = ["word"]
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.word)
        super(Word, self).save(*args, **kwargs)
    def definition(self):
        try:
            return self.definitions.filter(approved=True)[0]
        except:
            return None
    def authors(self):
        return [definition.user if definition.user else "anonymous" for definition in self.definitions.all()]   
   
    
    def get_absolute_url(self):
        return reverse('update-word', kwargs={'slug': self.slug})   
    
class Definition(models.Model):
     definition = models.CharField(max_length=200)
     up_vote = models.IntegerField(default=0,blank = True)
     down_vote = models.IntegerField(default=0,blank = True)
     approved = models.BooleanField(default=False)
     user = models.ForeignKey(settings.AUTH_USER_MODEL,blank = True, null = True)
     word = models.ForeignKey(Word, null = True,related_name='definitions')
          
        
     def __unicode__(self):
        return self.definition
     
     
     