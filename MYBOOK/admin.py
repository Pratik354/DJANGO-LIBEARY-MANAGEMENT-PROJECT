from django.contrib import admin
from MYBOOK.models import bookapp

class RegisAdmin(admin.ModelAdmin):
    list_display=("user",'id',"stud_id","book_name","auther_name","date","status")
admin.site.register(bookapp,RegisAdmin)