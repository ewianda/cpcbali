from django.contrib import admin
from dictionary.models import Word,Definition
from actions.action import socialize
# Register your models here.
class  DefinitionInline(admin.TabularInline):
      model = Definition 
class WordAdmin(admin.ModelAdmin):
    inlines = [
               DefinitionInline
    ]

    actions = [socialize]


admin.site.register(Word,WordAdmin)