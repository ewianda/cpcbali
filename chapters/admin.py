from django.contrib import admin
from chapters.models import Chapter,ChapterMember
# Register your models here.
class MemberInlineAdmin(admin.TabularInline):
    model = ChapterMember
    extra = 1
class ChapterAdmin(admin.ModelAdmin):
    inlines = [
       MemberInlineAdmin
    ]
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Chapter,ChapterAdmin)