from __future__ import unicode_literals
from django.db import models

# Create your models here.
#-*- coding: utf-8 -*-


from datetime import datetime
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

from django.core.urlresolvers import reverse
class PublicManager(models.Manager):
    """Returns published articles that are not in the future."""
    
    def published(self):
        return self.get_query_set().filter(publish__lte=datetime.now())


@python_2_unicode_compatible
class Topic(models.Model):
    """Story that accepts comments."""

    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique=True)
    body = RichTextField('body')
    allow_comments = models.BooleanField('allow comments', default=True)
    publish = models.DateField(default=datetime.now())
    objects = PublicManager() 

    class Meta:
        db_table = 'stories'
        ordering = ('-publish',)
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __str__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('topic-detail', (),{'slug': self.slug})
      
      
      
      
      
      