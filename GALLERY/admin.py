from django.contrib import admin
from GALLERY.models import courser,image

class RegisAdmin(admin.ModelAdmin):
    list_display=("image","date")
admin.site.register(courser,RegisAdmin)

class RegisAdmin(admin.ModelAdmin):
    list_display=("IMAGE",'date')
admin.site.register(image,RegisAdmin)