from django.contrib import admin
from dictionary.models import Word,Definition

# Register your models here.
class  DefinitionInline(admin.TabularInline):
      model = Definition 
class WordAdmin(admin.ModelAdmin):
    inlines = [
               DefinitionInline
    ]




admin.site.register(Word,WordAdmin)