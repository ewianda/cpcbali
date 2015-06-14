from django.db import models

# Create your models here.
class Anthem(models.Model):
    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique=True)
    @models.permalink
    def get_absolute_url(self):
        return ('anthem', (),{'slug': self.slug})
    def __str__(self):
        return '%s' % self.title