from django.contrib import admin
from history.models import  History,Principal,PrincipalBiography
# Register your models here.
# Register your models here.
class  BioInline(admin.TabularInline):
      model = PrincipalBiography 
class PrincipalAdmin(admin.ModelAdmin):
    inlines = [
             BioInline
    ]



class HistoryAdmin(admin.ModelAdmin):    
    prepopulated_fields = {"slug": ("name",)}
    
    
admin.site.register(Principal,PrincipalAdmin)    
admin.site.register(History,HistoryAdmin)