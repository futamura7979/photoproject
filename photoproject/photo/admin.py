from django.contrib import admin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    
class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    
