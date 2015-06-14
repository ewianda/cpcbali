from django.contrib import admin
from history.models import  History,Principal
# Register your models here.
class HistoryAdmin(admin.ModelAdmin):    
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Principal)    
admin.site.register(History,HistoryAdmin)