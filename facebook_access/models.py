from django.db import models

# Create your models here.
class FaceBookAcessToken(models.Model):
    access_token = models.CharField(max_length=255)
    expiration = models.DateTimeField()
    def __unicode__(self):
        return self.access_token
    