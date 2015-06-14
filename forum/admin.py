from django.contrib import admin
from forum.models import Topic
# Register your models here.

class TopicAdmin(admin.ModelAdmin):    
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Topic,TopicAdmin)