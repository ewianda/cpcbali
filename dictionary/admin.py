from django.contrib import admin
from dictionary.models import Word

# Register your models here.


class WordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Word)