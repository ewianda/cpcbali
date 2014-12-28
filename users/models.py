"""
This code was copied from https://docs.djangoproject.com/en/1.5/topics/auth/customizing/#a-full-example
Little modifications to accomodate the need for this site

Author Elvis Wianda

"""



from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django_thumbs.db.models import ImageWithThumbsField
import os
from datetime import date

from ckeditor.fields import RichTextField


UPLOAD_TO = getattr(settings, 'USERS_UPLOAD_TO', 'CpcUsers')

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Secret', 'Secret'),
)

def file(self, filename):
        ext = filename.split('.')[-1]
        file='{}.{}'.format(self.pk, ext)
        url = UPLOAD_TO + file
        fullname = os.path.join(settings.MEDIA_ROOT, url)
        if os.path.exists(fullname):
            os.remove(fullname)
            ad=fullname.split('.')[0]
            dd=ad + '*'
            print ad
            os.system('rm ' +dd)
        return url

def batch(self, filename):
        ext = filename.split('.')[-1]
        file='{}.{}'.format(self.pk, ext)
        url = "images/batch/" + file
        fullname = os.path.join(settings.MEDIA_ROOT, url)
        if os.path.exists(fullname):
            os.remove(fullname)
            ad=fullname.split('.')[0]
            dd=ad + '*'
            print ad
            os.system('rm ' +dd)
        return url

HOUSE_CHOICE=(
        ('ONEIL','ONEIL'), ('SAKER','SAKER'), ('KANGSEN','KANGSEN'), ('VILLERHEUR','VILLERHEUR'),
        ('GRESS','GRESS'), ('FONYONGA','FONYONGA'), ('ASHILI','ASHILI'), ('BUNGALOW ONE','BUNGALOW TWO'),
        ('BUNGALOW ONE','BUNGALOW THREE'),('BUNGALOW ONE','BUNGALOW FOUR'),('BUNGALOW ONE','BUNGALOW FIVE'),
        ('BUNGALOW ONE','BUNGALOW SIX')
        )
ROOM_CHOICE=[('ROOM  ' + str(i), 'ROOM  ' + str(i) ) for i in range(1,27)]
YEARS=[( str(i),  str(i) ) for i in range(1,8)]
YEARS_IN_BALI = [(str(i),  str(i) ) for i in range(1954,date.today().year)]


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),date_joined=now,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Boban(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('staff status'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_admin = models.BooleanField(_('Is Admin'), default=False)
    gender =  models.CharField(max_length=10, choices=GENDER_CHOICES)
    nickname = models.CharField(max_length=128,verbose_name='Nickname')
    years = models.CharField(_('Years in Bali'),max_length = 32,null=True, blank = True,choices=YEARS,default="7")
    end_date = models.CharField(_('Batch of'),max_length = 32,null=True, blank = True,choices=YEARS_IN_BALI ,default="1954")
    house =  models.CharField(_('House/Bungalow'), max_length = 32, blank = True,choices=HOUSE_CHOICE,default="ONEIL")
    room =  models.CharField(_('Dorm/Room'), max_length = 32, blank = True,choices=ROOM_CHOICE,default="ROOM 1")
    memoire=  RichTextField(_('Fun memories'), max_length = 255, blank = True)
    country = models.CharField(_('Country'), max_length = 100, blank = True)
    city = models.CharField(_('City'), max_length = 100, blank = True)
    picture =  ImageWithThumbsField(upload_to=file, blank = True, sizes=((125,125),(200,200)))
    notification = models.BooleanField(_('Receive info about Boba events'),default=True)

    objects =MyUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Batch(models.Model):
    picture =  ImageWithThumbsField(upload_to=batch, blank = True, sizes=((125,125),(200,200)))
    end_date = models.CharField(_('Batch of'),max_length = 32,null=True, blank = True,choices=YEARS_IN_BALI ,default="1954")
    def __unicode__(self):
	 return self.end_date
    def get_absolute_url(self):
        return reverse('batch')