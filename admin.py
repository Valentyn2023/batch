from django.contrib import admin
from ads2.models import Ad

# Register your models here.

#we want the admin UI to leave the picture and content_type alone

#define the AdAdmin class
class AdAdmin(admin.ModelAdmin):
    exclude= ('picture', 'content_type')
    
#register the admin class with the associated model   
 
admin.site.register(Ad, AdAdmin)