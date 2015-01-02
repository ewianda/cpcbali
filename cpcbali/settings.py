"""
Django settings for cpcbali project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-b$l!d^zps0ea!gts%wmrr9pxhl-fp%x(k$606zp1cf&r$wqrr'
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
   'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users', 'social.apps.django_app.default',
    'crispy_forms','dictionary','captcha','scholarship',
    'django.contrib.comments','django_comments_xtd',
     'registration',
      'ckeditor','home','chapters',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cpcbali.urls'

WSGI_APPLICATION = 'cpcbali.wsgi.application'
CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {

        'height': 300,
        'width': 500,
    },
}
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}
STATICFILES_DIRS = (
         os.path.join(BASE_DIR, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
)



TEMPLATE_DIRS = (
           os.path.join(BASE_DIR, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MEDIA_ROOT =os.path.join(BASE_DIR, 'images/')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

MEDIA_URL = '/images/'
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'social.backends.yahoo.YahooOAuth',
    'social.backends.linkedin.LinkedinOAuth',
    'social.backends.linkedin.LinkedinOAuth2',
    'social.backends.yahoo.YahooOpenId',
   'django.contrib.auth.backends.ModelBackend',
)

COMMENTS_APP = "django_comments_xtd"
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
USE_TZ = True


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = 'Your Registration With LSCDS'
SEND_ACTIVATION_EMAIL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile'


AUTH_USER_MODEL = 'users.Boban'
SOCIAL_AUTH_USER_MODEL = 'users.Boban'


SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
   # 'social.pipeline.mail.mail_validation',
   # 'lscds_site.pipeline.require_email',
    'cpcbali.pipeline.social_extra_data',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'cpcbali.pipeline.user_details_complete'
)

USER_FIELDS = ['email']
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL=True
USERNAME_IS_FULL_EMAIL=True

SOCIAL_AUTH_LINKEDIN_KEY='75epozhfxnkl2e'
SOCIAL_AUTH_LINKEDIN_SECRET='SnevZhT73Nfauqsu'
SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress',]
SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address'),
                                   ('headline', 'headline'),
                                   ('industry', 'industry')]



# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['first_name', 'last_name', 'email',
#                                         'username']
CRISPY_TEMPLATE_PACK = 'bootstrap3'

USERNAME_IS_FULL_EMAIL=True
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
SITE_ID = 1
SOCIAL_AUTH_NEW_USER_REDIRECT_URL =  '/'
STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC_URL')


COMMENTS_XTD_MAX_THREAD_LEVEL = 0
COMMENTS_APP = "django_comments_xtd"
EMAIL_HOST          = "smtp.gmail.com"
EMAIL_PORT          = "587"
EMAIL_USE_TLS       = True # Yes for Gmail
DEFAULT_FROM_EMAIL  = "Alice Bloggs <alice@example.com>"
SERVER_EMAIL        = DEFAULT_FROM_EMAIL
COMMENTS_XTD_CONFIRM_EMAIL = False


try:
    from local_settings import *
except ImportError:
    pass
