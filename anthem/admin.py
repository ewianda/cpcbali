from django.contrib import admin
from anthem.models import Anthem
# Register your models here.



class AnthemAdmin(admin.ModelAdmin):    
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Anthem,AnthemAdmin)